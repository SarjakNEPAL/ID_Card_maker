import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import sqlite3


global s
s=True

app=tk.Tk()
app.title("ID generator")
app.iconbitmap("assets/main.ico")
app.geometry("1000x500")
app.resizable(False,False)


#login frame
main=Frame(app,width=1000,height=500)
main.config(bg="#5585b5")
main.place(x=0,y=0)

#Canvas framings
Ad=Frame(main,width=400,height=480)
Mfrm=Frame(main,width=500, height=200,bg="#53a8b6")
creator=Frame(main,width=500,height=50,bg="#53a8b6")
Tit=Frame(main,width=500,height=70,bg="#bbe4e9")
subti=Frame(main,width=500,height=50,bg="#bbe4e9")
Tit.place(x=450,y=30)
subti.place(x=450,y=110)
Ad.place(x=10,y=35)
Mfrm.place(x=450,y=170)
creator.place(x=450,y=440)

#imagings
Ad_img=Image.open("assets/id-card.png")
ad_pic=ImageTk.PhotoImage(Ad_img.resize((400, 440)))
adlabel=Label(Ad,image=ad_pic,bg="#79c2d0")
adlabel.pack()

#exit func
def ext():
    app.destroy()


#Default Prompts
title=Label(Tit,text="ID-Generator",font=('Helvetica', 30),bg="#bbe4e9")
subtitle=Label(subti,text="Login",font=('Helvetica', 25),bg="#bbe4e9")
title.place(x=150,y=6)
subtitle.place(x=200,y=5)

def checkfld():
    username=user1.get()
    password=pass1.get()
    if username !='':
        if password!='' and len(password)>7:
            messagebox.showinfo("Stage 1 check",f"Hi {username} Login page will now exit")
        else:
            messagebox.showwarning("Password error","Password must contain more than 7 characters")
    else:
        messagebox.showwarning("Warning!","Username must not be blank")

def reg():
    def regst():
        messagebox.showinfo("Registration complete")
    def lg():
        subtitle.config(text="Login")
        Bttn2.config(text="Register", command=reg, bg="Black")
        Bttn.config(text="Login",command=checkfld)
    subtitle.config(text="Register")
    Bttn.config(text="Register", command=regst)
    Bttn2.config(text="Login",command=lg)


#Default entries
crtr=Label(creator,text="|||| Created By - Sarjak Bhandari ||||",font=('Helvetica', 20),bg="#bbe4e9")
usrnmr_=Label(Mfrm,text="Username:",font=('Helvetica', 25),bg="#53a8b6")
pss_=Label(Mfrm,text="Password:",font=('Helvetica', 25),bg="#53a8b6")
Bttn=Button(Mfrm,text="Login",bg="#ececec",height=1,width=10,font=('Helvetica', 20),command=checkfld)
Bttn2=Button(Mfrm,text="Register",bg="#ececec",height=1,width=10,font=('Helvetica', 20),command=reg)
Button(main,text="Exit",command=ext,font=('Helvetica', 20),bg="#bbe4e9",width=30,height=1).place(x=455,y=380)
#inputs
global username
global password



user1=Entry(Mfrm,font=('Helvetica', 20))
pass1=Entry(Mfrm,font=('Helvetica', 20))

crtr.place(x=40,y=5)
usrnmr_.place(x=20,y=10)
pss_.place(x=20,y=70)
Bttn.place(x=50,y=130)
Bttn2.place(x=250,y=130)
user1.place(x=185,y=15)
pass1.place(x=185,y=75)

#login function

app.mainloop()




































