from common import *

xpathsStr = {"title": "data-ec-name", "author": "data-ec-d1" \
    , "brand": "data-ec-brand", "genre": "data-ec-d3", "remixers": "data-ec-d2"}
xpathsInt = {"id": "data-ec-id", today(): "data-ec-position"}


values={"title": "NA", "artist": "NA", "brand": "NA", \
                "genre": "NA","id":"NA", today():"NA"}



def getStrValue(domElement, attrib):
    #print "check for "+attrib
    if attrib in domElement.attrib :
        return str(domElement.xpath("@"+attrib)[0])
        print "xpath found :)"
    else:
        #print "xpath not found :("
        return "NA"


def getIntValue(domElement, attrib):
    if attrib in domElement.attrib:
        return int(domElement.xpath("@"+attrib)[0])
    else:
        return "NA"

def getRealese(domElement):
    #p.buk-track-released
    #print vars(domElement)
    # div[3] / p[6]
    return str(domElement.xpath('div[3] / p[6]')[0].text_content())

def fromDOM(domElement):
    song = {}
    names1 = xpathsStr.keys()
    names2 = xpathsInt.keys()
    for field in names1:
        song[field] = getStrValue(domElement, xpathsStr[field])

    for field in names2:
        song[field] = getStrValue(domElement, xpathsInt[field])
    song["release"]=getRealese(domElement)


    return song