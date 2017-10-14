import datetime

def today():
    return day(datetime.datetime.today());

def day(dt):
    return str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)

