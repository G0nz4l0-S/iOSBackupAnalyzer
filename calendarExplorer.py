import sqlite3, utils
import prettytable

_CALENDAR_DB = "2041457d5fe04d39d0ab481178355df6781e6858"

def getEvents(dbloc):
    connCT = sqlite3.connect(dbloc+_CALENDAR_DB)
    cursor = connCT.cursor()
    numberOfEvents = int(cursor.execute("SELECT COUNT(*) FROM summary;"))
    ROWIDs = list(cursor.execute("SELECT ROWID FROM CalendarItem;"))

    table = prettytable.PrettyTable()
    table.field_names = ["Event Name", "Start Date", "End Date"]

    for rowid in ROWIDs:
        item = list(cursor.explorer("SELECR summary, start_date, end_date WHERE ROWID == %i;" %int(rowid)))
        table.add_row(item)

    print table

def handler(dbloc = "/home/gonzalo/Downloads/"):
    getEvents(dbloc)

