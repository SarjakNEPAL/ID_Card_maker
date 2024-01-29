from condata import *
from tkinter import messagebox
from tkinter import filedialog


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
        print(u,Fname,Gender,Phone)
        messagebox.showinfo("Datasaved","Your card will be made shortly")
    else:
        messagebox.showwarning("Warning","Please fill all the fields")


def chapic(user):
    cursor.execute("SELECT * FROM user_img WHERE username=?",[user])
    a=cursor.fetchone()
    if a==None or a=="" or a==0:
        return False
    else:
        return True
    
global filelocation
def saveimage(u):
    if chapic(u)==False:
         global get_image,filelocation
         get_image= filedialog.askopenfilenames(title="SELECT IMAGE", filetypes=(("png","*.png"),('jpg',"*.jpg"),("All Files","*.*")))
         filelocation=get_image[0]


def convert_image_into_binary(filename):
    with open(filename,"rb")as file:
        photo_image=file.read()
    return photo_image

def insert_image(u):
    insert_photo=convert_image_into_binary(get_image[0])
    cursor.execute("INSERT INTO user_img VALUES(?,?)",(u,insert_photo))
    link.commit()

def getfilelocation():
    global filelocation
    return filelocation

if __name__=="__main__":
    print(fetchgar('Sarjak'))