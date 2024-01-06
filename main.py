import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3


app=tk.Tk()
app.title("ID generator")
app.iconbitmap("assets/main.ico")
app.geometry("800x600")
app.resizable(False,False)
main=Frame(app)
bgimg=tk.PhotoImage("/assets/bklg.jpg")
bgimg_Label=Label(main,image=bgimg)
bgimg_Label.pack()
main.place(x=0,y=0)
app.mainloop()




































