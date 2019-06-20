import sqlite3, prettytable
import utils

_NOTES_DB = "ca3bc056d4da0bbf88b5fb3be254f3b7147e639c"
def getNotes(dbloc):
    connCT = sqlite.connect(dbloc+_NOTES_DB)
    cursor = connCT.cursor()
    numberOfNotes = int(list(cursor.execute("SELECT COUNT(*) FROM ZNOTEBODY"))[0][0])
   
   table = prettytable.PrettyTable()
   table.field_names = ["Note ID [Z_PK]","Author", "Creation Date", "Modification Date", "Note Body"]
   
   for i in range(1, numberOfNotes+1):
        note_item = list(cursor.execute("SELECT ZAUTHOR, CREATIONDATE, MODIFICATIONDATE FROM ZNOTE WHERE Z_PK == %i;" %i))
        note_body = list(cursor.execute("SELECT ZCONTENT FROM ZNOTEBODY WHERE Z_PK == %i" %i))[0][0]
        note = [note_item[0][0], utils.iOSTimeToDate(note_item[0][1]), utils.iOSTimeToDate(note_item[0][2], note_body)
