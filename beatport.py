# -*- coding: utf-8 -*-
# html.audiopreload body div#pjax-target div#pjax-inner-wrapper.pjax-inner-wrapper section.page-content-container main.interior div.full-col div.bucket.tracks.top-hundred-tracks ul.bucket-items.ec-bucket li.bucket-item.ec-item.track
import urllib2
import lxml.html
import pprint
import datetime
from Song import *
from common import *


def getList(html):
    """
    Get the list of the songs in the chart.

    @type string
    @param html the web page of the chart.

    @return an array with the DOM elements.
    """
    tree = lxml.html.fromstring(html)
    tracks = tree.cssselect('li.bucket-item.ec-item.track')
    return tracks


def checkPerformed():
    """
    Checks if the data has been revieved today.

    @return true if the data has already retrived today. False otherwise.
    """
    return False





def checkValidSong(track):
    res = False
    if 'data-ec-id' in track.attrib and str(track.xpath("@data-ec-id")[0]) != "":
        # pprint.pprint(str(track.xpath("@data-ec-id")[0]))
        res = True
    if track == []:
        res = False
    return res





if __name__ == '__main__':
    html = urllib2.urlopen('https://www.beatport.com/top-100').read()
    tracks = getList(html)
    today = day(datetime.datetime.today());
    # pprint.pprint (tracks)
    songs=[]
    for track in tracks:
        if checkValidSong(track):
            song = songBuilder(track)
            songs.append(song)







