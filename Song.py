##
# @file
# Makes some tasks related to extract information from the webpage
#


from common import *

'''
@param xpathsStr a list of fields and its xpath expression to find them
'''
xpathsStr = {"title": "data-ec-name", "author": "data-ec-d1" \
    , "brand": "data-ec-brand", "genre": "data-ec-d3", "remixers": "data-ec-d2"}

'''
@param xpathsInt a list of fields and its xpath expression to find them
'''
xpathsInt = {"id": "data-ec-id", today(): "data-ec-position"}

'''
@param values the initial dictionary that will be changed with the extracted values
'''
values={"title": "NA", "artist": "NA", "brand": "NA", \
                "genre": "NA","id":"NA", today():"NA"}



def getStrValue(domElement, attrib):
    '''

    @param domElement the piece of the webpage where one song lives
    @param attrib the attribute that we are looking for (without @)
    @return the value of the attribute or NA if is not found
    '''
    #print "check for "+attrib
    if attrib in domElement.attrib :
        return str(domElement.xpath("@"+attrib)[0])
        print "xpath found :)"
    else:
        #print "xpath not found :("
        return "NA"


def getIntValue(domElement, attrib):
    '''
    Retrieve an int value from a DOM element

    @param domElement: A DOM element containing a song
    @param attrib: the attribute to extract (without @)
    @return: the text content in the attribute or NA
    '''
    if attrib in domElement.attrib:
        return int(domElement.xpath("@"+attrib)[0])
    else:
        return "NA"

def getRealese(domElement):
    '''
    Get the release date

    @param domElement:   A DOM element containing a song
    @return: the text content with the release date
    '''
    #p.buk-track-released
    #print vars(domElement)
    # div[3] / p[6]
    return str(domElement.xpath('div[3] / p[6]')[0].text_content())

def fromDOM(domElement):
    '''
    Builds a dictionary containing a the data of one song
    @param domElement: A DOM element containing a song
    @return: a dict with the song data
    '''
    song = {}
    names1 = xpathsStr.keys()
    names2 = xpathsInt.keys()
    for field in names1:
        song[field] = getStrValue(domElement, xpathsStr[field])

    for field in names2:
        song[field] = getStrValue(domElement, xpathsInt[field])
    song["released"]=getRealese(domElement)


    return song