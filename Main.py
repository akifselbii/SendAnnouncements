#String.py dosyasına email atacak mail adresini ve şifresini girin
#Enter the e-mail address and password in the String.py file
#Mehmet Akif Selbi

import String as st
import DatabaseManager as dbm
import TerminalManager as tm
import GUInterface as gui
import sys

def Body():
    print(st.helpCommand)
    print(st.interfaceCommand)
    print(st.mailCommand)
    print(st.announcementsCommand)
    print(st.createAnnouncement)
    print(st.startCommand)
    print(st.deleteStartCommand)
    print(st.exitCommand)



def Terminal():
    Body()
    while(True):
        inpt = input(st.inpt)
        if(inpt == st._helpCommand):
            Body()

        elif(inpt == st._interfaceCommand):
            gui.Start()

        elif(inpt == st._mailCommand):
            tm.MailFunction()

        elif(inpt == st._announcementsCommand):
            faculty = tm.FacultyList()
            
            print(st.facultyList[faculty-1])
            if(st.facultyList[faculty-1][-1] == '.'):
                for i in tm.Announcements(faculty-1,0):
                    print(i)
            else:
                department = tm.DepartmentList(faculty)
                for i in tm.Announcements(faculty-1,department-1):
                    print(i)

        elif(inpt == st._createAnnouncement):
            subject = input(st.subject)
            body = input(st.body)
            print(st.zero)
            faculty = tm.FacultyList()
            
            if(faculty == 0):
                tm.CreateAnnouncement(subject,body,faculty-1)
            elif(st.facultyList[faculty-1][-1] == '.'):
                tm.CreateAnnouncement(subject,body,faculty-1,-1)
            else:
                print(st.zero)
                department = tm.DepartmentList(faculty)         
                tm.CreateAnnouncement(subject,body,faculty-1,department-1)

        elif(inpt == st._startCommand):
            Time,Num = tm.BeforeStart()
            tm.Start(Time,Num)

        elif(inpt == st._deleteStartCommand):
            dbm.DeleteAllLinks()
            Time,Num = tm.BeforeStart()
            tm.Start(Time,Num)

        elif(inpt == st._exitCommand):
            sys.exit(0)

        else:
            print(st.wrongEntry)
            continue

def Main():
    Terminal()
    
Main()
