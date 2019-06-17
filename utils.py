import datetime

def iOSTimeToDate(date):
    unixTS = 978307200
    Date = datetime.datetime.fromtimestamp(unixTS + date).strftime("%Y-%m-%d")
    return Date

def formatContactInfo(ctinfo):
    pass
