import sqlite3, prettytable
import utils

# ---------------------------------------------
#Cosas a cambiar:
#   (*) Modo de conseguir dbloc? = [
#       $ Un programa main?
#       $ Una funcion ?
#   ]
#----------------------------------------------

_CONTACTS_DB = "31bb7ba8914766d4ba40d6dfb6113c8b614be442"

def getContacts(dbloc):
    connCT = sqlite3.connect(dbloc+_CONTACTS_DB)
    cursor = connCT.cursor()
    numberOfContacts = int(str(list(cursor.execute("SELECT COUNT(*) FROM ABPerson;"))[0][0]))
    contacts = {}
    for i in range(1, numberOfContacts+1):
        contacts[i] = list(cursor.execute("SELECT First, Last, Birthday FROM ABPerson WHERE ROWID == %i;" %i))
    connCT.close()
    return contacts

def getContactInfo(contacts, dbloc):
    connCT = sqlite3.connect(dbloc+_CONTACTS_DB)
    cursor = connCT.cursor()
    length = len(contacts)
    for i in range(1, length+1):
        print contacts[i]
        print
        ctinfo = list(cursor.execute("SELECT value FROM ABMultiValue WHERE record_id == %i;" %i));
        contacts[i] = [contacts[i],(list(ctinfo))]
    connCT.close()
    return contacts
  

def handler(dbloc):
    for i in getContactInfo(getContacts(dbloc), dbloc).values():
        print i
    table = prettytable.PrettyTable()
    table.field_names = ["record_id", "Name", "Last", "Birthday", "Contact Info"]
    p = 1
    for i in getContactInfo(getContacts()).values():
        date = ""
        try:
            date = utils.iOSTimeToDate(i[0][0][2])
        except TypeError:
            date = "----"

        table.add_row([str(p),i[0][0][0], i[0][0][1], date, utils.formatContactInfo(i[1], p)[1]])

    p += 1
    print table
 
