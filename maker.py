from condata import *
from tkinter import messagebox

def fetchgar(a):
    data={"FullName":"","gender":"","phone":0,"address":"","company":""}
    cursor.execute("SELECT Fname,gender,phone,address,company FROM user_info WHERE username=?",[a])
    a=cursor.fetchone()
    if a!=None:
        data["Fullname"]:a[0]
        data["Gender"]:a[1]
        data["phone"]:a[2]
        data["address"]:a[3]
        data["company"]:a[4]
        print(data)
        return data

def hal(u,Fname,Gender,Phone,Address,Company,Picture):
    if Fname!="" or Gender !="" or Phone!="" or Address!="":
        # cursor.execute("INSERT INTO user_info VALUES(?,?,?,?,?,?)",[u,Fname,Gender,Phone,Address,Company])
        # link.commit()
        print(u,Fname,Gender,Phone)
        messagebox.showinfo("Datasaved","Your card will be made shortly")
    else:
        messagebox.showwarning("Warning","Please fill all the fields")



    