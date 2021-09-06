#Mehmet Akif Selbi

from tkinter import *
import GUInterfaceManager as guim
import String as st
import TerminalManager as tm
import DatabaseManager as dbm

def Start():
    def raiseFrame(frame,ch):
        frame.tkraise()
        global choice
        choice = ch

    def FindIndex(value,stList):
        for i in range(len(stList)):
            if(value == stList[i]):
                return i

    def RefreshAnnouncements(value1):
        value1 = valueInside.get()
        value2 = valueInside2.get()

        temp = value2
        value1 = FindIndex(value1,st.facultyList)
        value2 = FindIndex(value2,st.departmentList[value1])

        textBox.configure(state = "normal")
        textBox.delete("0.0",END)
        textBox.insert(END,">>>>>>>>>  "+temp+"  <<<<<<<<<")
        textBox.insert(END,"\n\n")
        for i in tm.Announcements(value1,value2):
            textBox.insert(END, str(i))
            textBox.insert(END,"\n\n")
        textBox.configure(state = "disabled")

    def DisplaySelected(value):
        global choice
        if(choice == 1):
            value = valueInside.get()
        if(choice == 2):
            value = valueInside3.get()
        if(choice == 3):
            value = valueInside5.get()

        if(value != st.allFacultySendI):
            value = FindIndex(value,st.facultyList)
        else:
            choice = None

        if(choice == 1):
            global valueInside2
            valueInside2 = StringVar(f1)
            valueInside2.set(st.departmentName)
            optionMenu2 = OptionMenu(f1,valueInside2,*st.departmentList[value],command=RefreshAnnouncements)
            optionMenu2.place(relx=0.25, rely=0.9,relwidth=0.5, relheight=0.07)
        if(choice == 2):
            global valueInside4
            valueInside4 = StringVar(f2)
            valueInside4.set(st.departmentName)
            optionMenu4 = OptionMenu(f2,valueInside4,*st.departmentList[value])
            optionMenu4.place(relx=0.01, rely=0.94,relwidth=0.5, relheight=0.05)
        if(choice == 3):
            dList = [st.allDepartmentSendI]
            for i in st.departmentList[value]:
                dList.append(i)

            global valueInside6
            valueInside6 = StringVar(f3)
            valueInside6.set(st.allDepartmentSendI)
            optionMenu6 = OptionMenu(f3,valueInside6,*dList)
            optionMenu6.place(relx=0.25, rely=0.73,relwidth=0.5, relheight=0.06)

    def Error():
        textBoxMail.configure(state = "normal")
        textBoxMail.delete("0.0",END)
        textBoxMail.insert(END, st.warningI)
        textBoxMail.insert(END,"\n\n")
        textBoxMail.configure(state = "disabled")

    def Add():
        try:
            name = nameEntry.get("1.0",'end-1c').strip()
            nameEntry.delete("0.0",END)
            mail = mailEntry.get("1.0",'end-1c').strip()
            mailEntry.delete("0.0",END)
            value1 = valueInside3.get()
            valueInside3.set(st.facultyName)
            value2 = valueInside4.get()
            valueInside4.set(st.departmentName)
        
            if(value2 != None and value1 != st.facultyName and value2 != st.departmentName):
                data = [mail,name,value1,value2]

                dbm.SaveMail(data)
                Refresh(dbm.GetData())
            else:
                Error()
        except:
            Error()

    def Delete():
        mail = mailEntry.get("1.0",'end-1c').strip()
        mailEntry.delete("0.0",END)
        dbm.DeleteMail(mail)
        Refresh(dbm.GetData())
        valueInside3.set(st.facultyName)
        try:
            valueInside4.set(st.departmentName)
        except:
            pass
        Refresh(dbm.GetData())

    def Find():
        name = nameEntry.get("1.0",'end-1c').strip()
        nameEntry.delete("0.0",END)
        mail = mailEntry.get("1.0",'end-1c').strip()
        mailEntry.delete("0.0",END)
        value1 = valueInside3.get()
        try:
            value2 = valueInside4.get()
        except:
            value2 = None
        valueInside3.set(st.facultyName)
        try:
            valueInside4.set(st.departmentName)
        except:
            pass

        if(value1 == st.facultyName):value1 = None
        if(value2 == st.departmentName):value2 = None
        data = dbm.FindData(mail,name,value1,value2)

        Refresh(data)

    def Refresh(data):
        textBoxMail.configure(state = "normal")
        textBoxMail.delete("0.0",END)
        
        textBoxMail.insert(END, st.mailSaveBox)
        textBoxMail.insert(END, "\n")
        for i in data:
            for j in i:
                textBoxMail.insert(END, str(j)+"  ")
            textBoxMail.insert(END, "\n")
        textBoxMail.configure(state = "disabled")

    def RefreshButtonFunction():
        textBoxMail.configure(state = "normal")
        textBoxMail.delete("0.0",END)
        
        textBoxMail.insert(END, st.mailSaveBox)
        textBoxMail.insert(END, "\n")
        for i in dbm.GetData():
            for j in i:
                textBoxMail.insert(END, str(j)+"  ")
            textBoxMail.insert(END, "\n")
        textBoxMail.configure(state = "disabled")

    def Send():
        subject = entryBoxSubject.get("1.0",'end-1c').strip()
        body = entryBoxBody.get("1.0",'end-1c').strip()
        value1 = valueInside5.get()
        if(value1 != st.allFacultySendI):
            value1 = FindIndex(value1,st.facultyList)
        try:
            value2 = valueInside6.get()
            if(value2 != st.allDepartmentSendI):
                value2 = FindIndex(value2,st.departmentList[value1])
        except:
            value2 = None

        if(value1 == None or value1 == st.allFacultySendI):
            tm.CreateAnnouncement(subject,body)
        elif(value2 == None or value2 == st.allDepartmentSendI):
            tm.CreateAnnouncement(subject,body,value1)
        else:
            tm.CreateAnnouncement(subject,body,value1,value2)

    def ProgramStart():
        time = entryBoxTime.get("1.0",'end-1c').strip()
        num = entryBoxNum.get("1.0",'end-1c').strip()
        window.destroy()
        if(time == None):time = 1
        if(num == None):num == 1
        try:
            tm.Start(int(time),int(num))
        except:
            tm.Start(1,1)

    def DeleteAllLinks():
        dbm.DeleteAllLinks()
        ProgramStart()

    window = Tk()

    guim.WindowSize(window,st.width,st.height)
    canvas = Canvas(window, height=st.height, width=st.width)
    canvas.pack()    

    frameUp = guim.FrameBox(window,0,0,1,0.05)

    f1 = guim.FrameBox(window,0,0.05,1,0.95)
    f2 = guim.FrameBox(window,0,0.05,1,0.95)
    f3 = guim.FrameBox(window,0,0.05,1,0.95)
    f4 = guim.FrameBox(window,0,0.05,1,0.95)

    #farmeUp
    button1 = guim.ButtonBox(frameUp,st.announcementsI,0,0,0.25,0.9,lambda:raiseFrame(f1,1))
    button2 = guim.ButtonBox(frameUp,st.saveMailI,0.25,0,0.25,0.9,lambda:raiseFrame(f2,2))
    button3 = guim.ButtonBox(frameUp,st.createAnnouncementI,0.50,0,0.25,0.9,lambda:raiseFrame(f3,3))
    button4 = guim.ButtonBox(frameUp,st.startI,0.75,0,0.25,0.9,lambda:raiseFrame(f4,4))

    #f1
    textBox = guim.TextBox(f1,0,0.01,0.97,0.8)
    valueInside = StringVar(f1)
    valueInside.set(st.facultyName)
    optionMenu = OptionMenu(f1,valueInside,*st.facultyList,command=DisplaySelected)
    optionMenu.place(relx=0.25, rely=0.82,relwidth=0.5, relheight=0.07)
    scrollbar = guim.ScrollBar(f1,0.97,0.01,0.03,0.8,textBox)
    textBox['yscrollcommand'] = scrollbar.set

    #f2
    textBoxMail = guim.TextBox(f2,0,0.01,0.97,0.7)

    name = guim.LabelBox(f2,st.nameI,0.01,0.76,0.1,0.05,10)
    mail = guim.LabelBox(f2,st.mailI,0.01,0.82,0.1,0.05,10)

    nameEntry = guim.EntryBox(f2,0.11,0.76,0.4,0.05)
    mailEntry = guim.EntryBox(f2,0.11,0.82,0.4,0.05)

    valueInside3 = StringVar(f2)
    valueInside3.set(st.facultyName)
    optionMenu3 = OptionMenu(f2,valueInside3,*st.facultyList,command=DisplaySelected)
    optionMenu3.place(relx=0.01, rely=0.88,relwidth=0.5, relheight=0.05)

    findButton = guim.ButtonBox(f2,st.findI,0.55,0.76,0.4,0.06,Find)
    deleteButton = guim.ButtonBox(f2,st.deleteI,0.55,0.83,0.4,0.06,Delete)
    saveButton = guim.ButtonBox(f2,st.saveI,0.55,0.90,0.4,0.06,Add)
    refreshButton = guim.ButtonBox(f2,st.refreshI,0,0.70,1,0.05,RefreshButtonFunction)
    scrollbar2 = guim.ScrollBar(f2,0.97,0.01,0.03,0.69,textBoxMail)
    textBoxMail['yscrollcommand'] = scrollbar2.set

    #f3
    subject = guim.LabelBox(f3,st.subjectI,0.01,0.01,0.1,0.05,10)
    entryBoxSubject = guim.EntryBox(f3,0.12,0.01,0.8,0.05)
    body = guim.LabelBox(f3,st.bodyI,0.01,0.09,0.1,0.05,10)
    entryBoxBody = guim.EntryBox(f3,0.12,0.09,0.8,0.5)

    fList = [st.allFacultySendI]
    for i in st.facultyList:
        fList.append(i)

    valueInside5 = StringVar(f3)
    valueInside5.set(st.allFacultySendI)
    optionMenu5 = OptionMenu(f3,valueInside5,*fList,command=DisplaySelected)
    optionMenu5.place(relx=0.25, rely=0.63,relwidth=0.5, relheight=0.06)

    sendButton = guim.ButtonBox(f3,st.sendI,0.25,0.83,0.5,0.1,Send)

    #f4
    time = guim.LabelBox(f4,st.timeI,0.15,0.3,0.4,0.05,10)
    entryBoxTime = guim.EntryBox(f4,0.55,0.3,0.3,0.05)
    num = guim.LabelBox(f4,st.numI,0.15,0.4,0.4,0.05,10)
    entryBoxNum = guim.EntryBox(f4,0.55,0.4,0.3,0.05)

    startButton = guim.ButtonBox(f4,st.startI,0.3,0.5,0.4,0.1,ProgramStart)
    DeleteStartButton = guim.ButtonBox(f4,st.deleteStartI,0.3,0.65,0.4,0.1,DeleteAllLinks)


    window.mainloop()