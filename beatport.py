# -*- coding: utf-8 -*-
# html.audiopreload body div#pjax-target div#pjax-inner-wrapper.pjax-inner-wrapper section.page-content-container main.interior div.full-col div.bucket.tracks.top-hundred-tracks ul.bucket-items.ec-bucket li.bucket-item.ec-item.track
import lxml.html
import os
import urllib2

from Song import *
from common import *

cache_dir="cache"

def getList(url):
    """
    Get the list of the songs in the chart.

    @type string
    @param html the web page of the chart.

    @return an array with the DOM elements.
    """
    if not cache_dir in os.listdir('.'):
        os.mkdir(cache_dir)
    file = os.path.join(cache_dir, "beatport+list+"+today()+".html")
    html=None
    if os.path.isfile(file):
        #print "file exists"
        html=open(file,"r").read()
    else:
        html = urllib2.urlopen(url).read()
    tree = lxml.html.fromstring(html)
    open(file, 'wb').write(html)
    tracks = tree.cssselect('li.bucket-item.ec-item.track')
    return tracks

def checkValidSong(track):
    res = False
    if 'data-ec-id' in track.attrib and str(track.xpath("@data-ec-id")[0]) != "":
        #pprint.pprint(str(track.xpath("@data-ec-id")[0]))
        res = True
    if track == []:
        res = False
    return res





if __name__ == '__main__':
    verbose=True
    url='https://www.beatport.com/top-100'

    tracks = getList(url)
    today = day(datetime.datetime.today());
    # pprint.pprint (tracks)
    songs=[]
    for track in tracks:
        if checkValidSong(track):
            song = fromDOM(track)
            songs.append(song)
            if verbose:
                print song["id"]+" "+song["title"]+" -> retrieved"
                







