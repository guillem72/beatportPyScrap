import datetime

minHeaders=["title","author", "brand", "genre","id"]

def today():
    return day(datetime.datetime.today());

def day(dt):
    return str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)

def dict2String(dict):
    if isinstance(dict,dict):
        ms="{"
        ks=dict.keys()
        first=True
        for key in ks:
            if not first:
                ms=ms+","
            ms=ms+key+":"+dict[key]
            first = False
        return ms+"}"
    else:
        return "ERROR: Fuction dict2String expected a dict as argument"
