import datetime



def today():
    #return "15-10-2017"
    #return "16-10-2017"
    #return "17-10-2017"
    return day(datetime.datetime.today());

def day(dt):
    return str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)


def mergeDicts(d1,d2):
    k1=set(d1.keys())
    k2=set(d2.keys())
    if (k1==k2):
        return d1
    k=k1.union(k2)
    d={}
    for key in k:
        if key in k1:
            d[key]=d1[key]
        else:
            d[key]=d2[key]
    return d


def dict2String(dict0):
    if isinstance(dict0,dict):
        ms="{"
        ks=dict0.keys()
        first=True
        for key in ks:
            if not first:
                ms=ms+","
            ms=ms+key+":"+str(dict0[key])
            first = False
        return ms+"}"
    else:
        return "ERROR: Fuction dict2String expected a dict as argument"
