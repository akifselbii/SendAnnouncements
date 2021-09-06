#Mehmet Akif SELBİ

import sqlite3
import String as st

def SaveMail(data):
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,faculty,department)""")

        try:
            im.execute("""INSERT INTO mailler VALUES (?,?,?,?)""",data)
        except:
            print(st.registeredUser)
        
        vt.commit()

def SaveLink(data):
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS linkler (id PRIMARY KEY,link)""")

        try:
            im.execute("""INSERT INTO linkler VALUES (?,?)""",data)
        except:
            pass
        vt.commit()

def GetLink(id):
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS linkler (id PRIMARY KEY,link)""")
        if(id):
            im.execute("SELECT link FROM linkler WHERE id = "+"'"+str(id)+"'")
            im = im.fetchall()
        else:
            im.execute("""SELECT id FROM linkler""")
        return im


def DeleteLink(id):
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("CREATE TABLE IF NOT EXISTS linkler (id PRIMARY KEY,link)")
        try:
            im.execute("DELETE FROM linkler WHERE id = ?",(str(id),))
        except:
            return

        vt.commit()

def DeleteAllLinks():
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("CREATE TABLE IF NOT EXISTS linkler (id PRIMARY KEY,link)")
        try:
            im.execute("DROP TABLE linkler")
        except:
            return

        vt.commit()

def GetData():
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,faculty,department)""")
        im.execute("""SELECT * FROM mailler""")

        return im
    
def GetMail():
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,faculty,department)""")
        im.execute("""SELECT mail FROM mailler""")
        
        return im
    
def DeleteMail(mail):
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,faculty,department)""")
        try:
            im.execute("DELETE FROM mailler WHERE mail = ?",(mail,))
        except:
            print(st.noMail)
        vt.commit()

def FindData(mail,name,faculty,department,choose):
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS mailler (mail PRIMARY KEY,isim,faculty,department)""")

        main = """SELECT * FROM mailler WHERE """
        andd = " AND "
        if(choose != None):
            main = main.replace("*","mail")
        if(mail):
            main += "mail = "+"'"+mail+"'"+andd
        if(name):
            main += "isim = "+"'"+name+"'"+andd
        if(faculty):
            main += "faculty = "+"'"+faculty+"'"+andd
        if(department):
            main += "department = "+"'"+department+"'"
        if(main[-5:] == " AND "):
            main = main.replace(" AND ","",-1)

        try:
            im.execute(main)
        except:
            return ""
        data = im.fetchall()

        if data:return data
        else: return ""
