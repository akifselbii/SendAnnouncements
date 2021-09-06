#Mehmet Akif Selbi

import String as st
import Database as db

def GetLink(faculty,department):
    link = db.GetLink(faculty+department)
    return link

def SaveLink(data):
    db.SaveLink(data)

def DeleteAllLinks():
    db.DeleteAllLinks()

def DeleteLink(faculty,department):
    db.DeleteLink(faculty+department)

def GetMail():
    return db.GetMail()

def GetData():
    return db.GetData()
            
def SaveMail(dbList):
    if(dbList[0] != ""):
        db.SaveMail(dbList)

def DeleteMail(mail):
    db.DeleteMail(mail)

def FindData(mail=None,name=None,faculty=None,department=None,choose=None):
    return db.FindData(mail,name,faculty,department,choose)