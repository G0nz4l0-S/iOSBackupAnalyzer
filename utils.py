import datetime

def iOSTimeToDate(date):
    unixTS = 978307200
    Date = datetime.datetime.fromtimestamp(unixTS + date).strftime("%Y-%m-%d")
    return Date

def formatContactInfo(ctinfo, ctID):
    ctinfo_list = []
    for i in range(len(ctinfo)):
        ctinfo_list.append(ctinfo[i][0])

    return [ctID, ctinfo_list]
    
