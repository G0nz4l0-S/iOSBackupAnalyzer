import sqlite3, utils
import prettytable

_CALENDAR_DB = "2041457d5fe04d39d0ab481178355df6781e6858"

def getEvents(dbloc):
    connCT = sqlite3.connect(dbloc+_CALENDAR_DB)
    cursor = connCT.cursor()
    numberOfEvents = int(list(cursor.execute("SELECT COUNT(*) FROM CalendarItem;"))[0][0])
    ROWIDs = list(cursor.execute("SELECT ROWID FROM CalendarItem;"))

    table = prettytable.PrettyTable()
    table.field_names = ["Event Name", "Start Date", "End Date"]

    for rowid in ROWIDs:
        item = list(cursor.execute("SELECT summary, start_date, end_date FROM CalendarItem WHERE ROWID == %i;" %int(rowid[0])))
        table.add_row([item[0][0], utils.iOSTimeToDate(item[0][1]), utils.iOSTimeToDate(item[0][2])])

    print table
    connCT.close()
def handler(dbloc = "/home/gonzalo/Downloads/backup/"):
    getEvents(dbloc)

handler()
