#Mehmet Akif Selbi

import String as st
import DatabaseManager as dbm
import Announcements as ac
import SendMail as sm
import time

def MailFunction():
    print(st.saveCommand)
    print(st.deleteCommand)
    print(st.listCommand)
    print(st.backCommand)
    while(True):
        inpt = input(st.inptMail)      
        if(inpt == st._saveCommand):
            name = input(st.name)
            mail = input(st.mail)

            faculty = FacultyList()
            department = DepartmentList(faculty)

            dbList = [mail,name,st.facultyList[faculty-1],st.departmentList[faculty-1][department-1]]
            dbm.SaveMail(dbList)
        elif(inpt == st._deleteCommand):
            mail = input(st.registeredMail)
            dbm.DeleteMail(mail)                
        elif(inpt == st._listCommand):
            for i in dbm.GetData():
                print(i)
        elif(inpt == st._backCommand):
            return
        else:
            print(st.wrongEntry)

def FacultyList():
    for i in range (len(st.facultyList)):
        print("     "+str(i+1)+"-"+st.facultyList[i])
    while(True):
        faculty = input(st.faculty)
        try:
            if(int(faculty) > -1 and int(faculty) < len(st.facultyList)+1 ):
                break
            else:
                print(st.wrongEntry)
        except:
            print(st.wrongEntry)
    return int(faculty)

def DepartmentList(faculty):
    for i in range(len(st.departmentList[int(faculty)-1])):
        print("     "+str(i+1)+"-"+st.departmentList[int(faculty)-1][i])
    while(True):
        department = input(st.department)
        try:
            if(int(department) > -1 and int(department) < len(st.departmentList)+1 ):
                break
            else:
                print(st.wrongEntry)
        except:
            print(st.wrongEntry)
    return int(department)

def Announcements(facultyNo,departmentNo):
    flag,subject= 1,[]
    for i in ac.Titles(facultyNo,departmentNo):
        if(flag == 2):subject.append(i)
        if(flag == 4):flag = 0
        flag += 1
    return subject

def BeforeStart():
    try:
        Num = int(input(st.numberOfMail))
    except:
        Num = 1
    try:
        Time = int(input(st.enterMinutes))
    except:
        Time = 1
    return Time,Num

def Send(_list,subject,body,facultyNo=-1,departmentNo=-1):
    if(facultyNo == -1):
        mails = dbm.GetMail()
    elif(departmentNo == -1):
        mails = dbm.FindData(faculty = st.facultyList[facultyNo],choose = 0)
    else:
        mails = dbm.FindData(faculty = st.facultyList[facultyNo],department = st.departmentList[facultyNo][departmentNo], choose = 0)
    for i in mails:
        for k in i:
            for j in range(len(_list)):
                try:
                    sm.Mail(subject[j],body[j],k)
                except:
                    continue

def CreateAnnouncement(sub="",bdy="",faculty=-1,department=-1):
    subject,body = [],[]
    subject.append(sub)
    body.append(bdy)
    Send(subject,subject,body,faculty,department)

def Start(Time,Num):
    while(True):
            if(Num>15):Num = 15
            elif(Num<1):Num = 1
                
            
            for i in range(len(st.facultyTagList)):
                for j in range(len(st.departmentTagList[i])):
                    if(dbm.FindData(faculty=st.facultyList[i],department=st.departmentList[i][j],choose=0)):
                        links = ac.Links(i,j)
                        try:
                            savedLink = dbm.GetLink(i,j)[0][0]
                        except:
                            savedLink = None
                        linkList = []
                        for k in links:
                            if(k == savedLink):
                                break
                            else:
                                linkList.append(k)
                        
                        if(len(linkList)>0):
                            try:
                                linkList = linkList[:Num]
                            except:
                                print(st.Error)
                            subject = Announcements(i,j)
                            subject = subject[:len(linkList)]
                            body = ac.Body(linkList)

                            Send(linkList,subject,body,i,j)
                
                            if(savedLink != None):
                                dbm.DeleteLink(i,j)
                            dbm.SaveLink([str(i+j),linkList[0]])
                        else:
                            print(st.departmentList[i][j]+st.noNewAnnouncements)
                    
            time.sleep(60*Time)



