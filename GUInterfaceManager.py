from tkinter import *

def FrameBox(window,x,y,w,h,bg="#56ffff"):
    frame = Frame(window, bg='#add8e6')
    frame.place(relx=x, rely=y,relwidth=w, relheight=h)
    return frame

def LabelBox(window,text,x,y,w,h,size,bg="#56ffff",fg="black",f1="verdana",f2="bold"):
    lbl = Label(window, text =text, fg=fg, bg=bg, font=(f1, size, f2))
    lbl.place(relx=x, rely=y,relwidth=w, relheight=h)
    return lbl

def TextBox(window,x,y,w,h,f1="Courier"):
    tb = Text(window)
    tb.config(font =(f1, 14), state=DISABLED)
    tb.place(relx=x, rely=y,relwidth=w, relheight=h)
    return tb

def ButtonBox(window,text,x,y,w,h,command,f1="Verdana",f2="bold",bg="#00007f",ab="#3c9d9b",fg='#ffffff'):
    button = Button(window, font=(f1,12,f2), text= text,bd=0, bg=bg, activebackground=ab, fg=fg, command= command)
    button.place(relx=x, rely=y,relwidth=w, relheight=h)
    return button

def EntryBox(window,x,y,w,h,bg="white",w1="1",h1="1",f1="Arial"):
    box = Text(window, bd=0, bg=bg,width=w1, height=h1, font=f1)
    box.place(relx=x, rely=y,relwidth=w, relheight=h)
    
    return box

def ScrollBar(window,x,y,w,h,command):
    scrollbar = Scrollbar(window, command=command.yview)
    scrollbar.place(relx=x, rely=y,relwidth=w, relheight=h)
    return scrollbar

def WindowSize(window,w,h):
    appWidth = w
    appHeight = h

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)

    window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')