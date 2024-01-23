from condata import *
from tkinter import messagebox

def fetchgar(g):
    data=[]
    cursor.execute("SELECT Fname,gender,phone,address,company FROM user_info WHERE username=?",[g])
    a=(cursor.fetchone()) 
    if a!=None:
        data.append(a[0])
        data.append(a[1])
        data.append(a[2])
        data.append(a[3])
        data.append(a[4])
        return data

def hal(u,Fname,Gender,Phone,Address,Company,Picture):
    if Fname!="" or Gender !="" or Phone!="" or Address!="":
        cursor.execute("INSERT INTO user_info VALUES(?,?,?,?,?,?)",[u,Fname,Gender,Phone,Address,Company])
        link.commit()
        messagebox.showinfo("Datasaved","Your card will be made shortly")
    else:
        messagebox.showwarning("Warning","Please fill all the fields")


if __name__=="__main__":
    print(fetchgar('Sarjak'))