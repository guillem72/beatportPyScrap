# -*- coding: utf-8 -*-
# html.audiopreload body div#pjax-target div#pjax-inner-wrapper.pjax-inner-wrapper section.page-content-container main.interior div.full-col div.bucket.tracks.top-hundred-tracks ul.bucket-items.ec-bucket li.bucket-item.ec-item.track
#li.bucket-item.ec-item.track div.buk-track-meta-parent p.buk-track-released
import lxml.html
import os
import urllib2

from IO import *
from Song import *
from common import *

cache_dir="cache"
fname="files/songs.csv"

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


def readcsv():

    if os.path.isfile(fname):
        io=IO(fname)
        return io.read()
    return []


def updateSong(songsCsv, song):
    id0=song["id"]
    for songcsv in songsCsv:
        if id0==songcsv["id"]:
            song.update(songcsv)
    return song



if __name__ == '__main__':
    verbose=True
    psongs=readcsv()

    url='https://www.beatport.com/top-100'
    tracks = getList(url)

    headers=set({})
    songs=[]
    for track in tracks:
        if checkValidSong(track):
            song = fromDOM(track)
            headers=headers.union(set(song.keys()))
            songs.append(song)
    io=IO(fname)
    io.write(songs,headers)








