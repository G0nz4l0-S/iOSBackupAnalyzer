import sqlite3, prettytable
import utils

_NOTES_DB = "ca3bc056d4da0bbf88b5fb3be254f3b7147e639c"
def getNotes(dbloc):
    connCT = sqlite3.connect(dbloc+_NOTES_DB)
    cursor = connCT.cursor()
    numberOfNotes = int(list(cursor.execute("SELECT COUNT(*) FROM ZNOTEBODY"))[0][0])
   
    table = prettytable.PrettyTable()
    table.field_names = ["Note ID [Z_PK]","Author", "Creation Date", "Modification Date", "Note Body"]
   
    for i in range(1, numberOfNotes+1):
         note_item = list(cursor.execute("SELECT ZAUTHOR, ZCREATIONDATE, ZMODIFICATIONDATE FROM ZNOTE WHERE Z_PK == %i;" %i))
         note_body = list(cursor.execute("SELECT ZCONTENT FROM ZNOTEBODY WHERE Z_PK == %i" %i))[0][0]
         note = [str(i), note_item[0][0],utils.iOSTimeToDate(float(note_item[0][1])), utils.iOSTimeToDate(float(note_item[0][2])), utils.HTMLToText(note_body)]
         table.add_row(note)
    connCT.close()
    print table

def printBasicNotesInfo(dbloc):
    table = prettytable.PrettyTable()
    table.field_names = ["Note ID [Z_PK]", "Note Title", "Creation Date"]
    connCT = sqlite3.connect(dbloc+_NOTES_DB)
    cursor = connCT.cursor()
    numberOfNotes = int(list(cursor.execute("SELECT COUNT(*) FROM ZNOTEBODY"))[0][0])
    for i in range(1, numberOfNotes+1):
        note_info = list(cursor.execute("SELECT Z_PK, ZTITLE, ZCREATIONDATE FROM ZNOTE WHERE Z_PK == %i" %i))
        table.add_row([note_info[0][0], note_info[0][1], utils.iOSTimeToDate(float(note_info[0][2]))])
    connCT.close()
    print table

def printNoteBody(z_pk, dbloc):
    connCT = sqlite3.open(dbloc+_NOTES_DB)
    cursor = connCT.cursor()
    note_body = list(c.execute("SELECT ZCONTENT FROM ZNOTEBODY WHERE Z_PK == %i" %z_pk))[0][0]
    print note_body
    connCT.close()

def shell(dbloc = "/home/gonzalo/Downloads/backup/"):
    # getNotes(dbloc)
    #printBasicNotesInfo(dbloc)
    def helpn():
        print "Available Options: "
        print "\t help: Prints this help"
        print "\t list: List available notes"
        print "\t getbody NOTEID: Prints the note body for Z_PK == NOTEID"
    while True:
        cmd = raw_input("NOTES >> ")
        cmdp = cmd.lower().split(" ")
        for i in range(len(cmdp)):
            if cmdp[0] == "help":
            helpn()
            if cmdp[i] == "list":
               getBasicNotesInfo(dbloc)
            if cmdp[i] == "getbody" and cmdp[i+1]:
                printNoteBody(cmdp[i+1], dbloc)
            else:
                print "Missing Note ID"
            if cmdp[0] in ["quit", "exit"]:
                return

shell()

