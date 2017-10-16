##
# @file
# Main file which performs the main tasks.
# Reads csv, retrieves the webpage if it is needed and
# creates and maintains the csv file
#

# -*- coding: utf-8 -*-
# html.audiopreload body div#pjax-target div#pjax-inner-wrapper.pjax-inner-wrapper section.page-content-container main.interior div.full-col div.bucket.tracks.top-hundred-tracks ul.bucket-items.ec-bucket li.bucket-item.ec-item.track
# li.bucket-item.ec-item.track div.buk-track-meta-parent p.buk-track-released
import lxml.html
import urllib2

from IO import *
from Song import *
from common import *

'''
@param cache_dir the directory were the webpages are stored.
'''
cache_dir="cache"

'''
@param fname the name and the route where the csv file will be placed.
'''
fname="files/songs.csv"

def getList(url):
    """
    Get the list of the songs in the chart. It downloads and stores the page once per day

    @type string
    @param url the address of the web page of the chart.

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

    """
    Check if a DOM element could be a song. It does it by checking a suitable id

    @param track the DOM element which is expected to contain a song
    @return a boolean which is true if the id exists. Notice that couldn't be a number
    """
    res = False
    if 'data-ec-id' in track.attrib and str(track.xpath("@data-ec-id")[0]) != "":
        #pprint.pprint(str(track.xpath("@data-ec-id")[0]))
        res = True
    if track == []:
        res = False
    return res


def readcsv():
    '''
    Read the csv file
    @return a list of songs (that are dictionaries) present in the csv file
    '''
    if os.path.isfile(fname):
        io=IO(fname)
        return io.read()
    return []


def updateSong(songsCsv, song):
    '''
    Enrich a song with the information stored in the csv file

    @param songsCsv the list of song retrieved from the csv file
    @param song a dictionary which represents a song
    @return the csv song merged with the current song
    '''
    id0=song["id"]
    for songcsv in songsCsv:
        if song["id"]==songcsv["id"]:
            song=mergeDicts(songcsv,song)
    return song



if __name__ == '__main__':
    verbose=True
    psongs=readcsv()
    io = IO(fname)
    url='https://www.beatport.com/top-100'
    tracks = getList(url)

    headers=io.getFieldnames()
    if today() not in headers:
        headers.append(today())
    songs=[]
    for track in tracks:
        if checkValidSong(track):
            song0 = fromDOM(track)
            song=updateSong(psongs,song0)
            songs.append(song)

    io.write(songs,headers)








