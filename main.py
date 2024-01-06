import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3


global s
s=True

app=tk.Tk()
app.title("ID generator")
app.iconbitmap("assets/main.ico")
app.geometry("1000x500")
app.resizable(False,False)
main=Frame(app,width=1000,height=500)
main.config(bg="#5585b5")
main.place(x=0,y=0)

#Canvas framings
Ad=Frame(main,width=400,height=480,bg="#79c2d0")
Mfrm=Frame(main,width=500, height=200,bg="#53a8b6")
creator=Frame(main,width=500,height=50,bg="#53a8b6")
Tit=Frame(main,width=500,height=70,bg="#bbe4e9")
subti=Frame(main,width=500,height=50,bg="#bbe4e9")
Tit.place(x=450,y=30)
subti.place(x=450,y=130)
Ad.place(x=10,y=10)
Mfrm.place(x=450,y=200)
creator.place(x=450,y=440)
#login
def logn():
    TTL=Label()


app.mainloop()




































