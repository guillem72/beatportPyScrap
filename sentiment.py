##
# @file
# Sentiment analysis file.
#
from textblob import TextBlob
from common import *


def adSentiment(song):
    '''
    Enrich the song information performing sentiment analysis on its title

    @param song a dictionary representing a song. Any dictioonary with a title field would be valid
    @return a dictionary with the fields polarity and subjectivity added.
    '''
    if "polarity"in song and "subjectivity" in song:
        return song
    senti=sentiment(song["title"])

    song=mergeDicts(song,senti)
    return song

def sentiment(text):
    '''
    Performs a sentiment analysis in a unique piece of text

    @param text the text to be analyzed
    @return a dict with the fields polarity and subjectivity
    '''
    blob = TextBlob(text)

    res={"polarity":blob.sentiment.polarity,"subjectivity":blob.sentiment.subjectivity}
    #print(blob.sentiment.polarity)
    return res

#print (sentiment("I love you, girl")["sub"])