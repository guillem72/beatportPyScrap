from common import *
import lxml.html

xpathsStr = {"title": "@data-ec-name", "author": "@data-ec-dl" \
    , "brand": "@data-ec-brand", "genre": "@data-ec-d3"}
xpathsInt = {"id": "@data-ec-id", today(): "@data-ec-position"}


values={"title": "NA", "artist": "NA", "brand": "NA", \
                "genre": "NA","id":"NA", today():"NA"}

def getStrValue(domElement, attrib):
    if attrib in domElement.attrib and str(domElement.xpath(attrib)[0]) != "":
        return str(domElement.xpath(attrib)[0])
    else:
        return "NA"


def getIntValue(domElement, attrib):
    if attrib in domElement.attrib:
        return int(domElement.xpath(attrib)[0])
    else:
        return "NA"


def songBuilder(domElement):
    names1 = xpathsStr.keys()
    names2 = xpathsInt.keys()
    for field in names1:
        values[field] = getStrValue(domElement, xpathsStr[field])
    for field in names2:
        values[field] = getStrValue(domElement, xpathsInt[field])
    song={}

    return song