from Person import Person
import sqlite3, prettytable
import utils

# ---------------------------------------------
#Cosas a cambiar:
#   (*) Tiempo iOS a ISO ---> TypeError [Linea 46] 

_CONTACTS_DB = "31bb7ba8914766d4ba40d6dfb6113c8b614be442"
_CALENDAR_DB = "2041457d5fe04d39d0ab481178355df6781e6858"
_NOTES_DB = "ca3bc056d4da0bbf88b5fb3be254f3b7147e639c"
_CALLHISTORY_DB = "2b2b0084a1bc3a5ac8c27afdf14afb42c61a19ca"
_LOCATIONS_DB = "4096c9ec676f2847dc283405900e284a7c815836"
 

# FOR iOS 11 and newer: _WEBHISTORY_DB = "e74113c185fd8297e140cfcf9c99436c5cc06b57" 
def getContacts():
    connCT = sqlite3.connect(dbloc+_CONTACTS_DB)
    cursor = connCT.cursor()
    numberOfContacts = int(str(list(cursor.execute("SELECT COUNT(*) FROM ABPerson;"))[0][0]))
    contacts = {}
    for i in range(1, numberOfContacts+1):
        contacts[i] = list(cursor.execute("SELECT First, Last, Birthday FROM ABPerson WHERE ROWID == %i;" %i))
    connCT.close()
    return contacts

def getContactInfo(contacts):
    connCT = sqlite3.connect(dbloc+_CONTACTS_DB)
    cursor = connCT.cursor()
    length = len(contacts)
    for i in range(1, length+1):
        print contacts[i]
        print
        ctinfo = list(cursor.execute("SELECT value FROM ABMultiValue WHERE record_id == %i;" %i));
        contacts[i] = [contacts[i],(list(ctinfo))]

    return contacts

for i in getContactInfo(getContacts()).values():
    print i
table = prettytable.PrettyTable()
table.field_names = ["Name", "Last", "Birthday", "Contact Info"]
for i in getContactInfo(getContacts()).values():
    try:
        table.add_row([i[0][0][0], i[0][0][1], utils.iOSTimeToDate(float(i[0][0][2])), i[[1][0]]])
    except TypeError:
        table.add_row([i[0][0][0], i[0][0][1], "---", i[[1][0]][0]])
    print i
    print

print table
   



