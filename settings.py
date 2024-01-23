from tkinter import *
from condata import *
from tkinter import messagebox
from scene2 import *
from maker import *

def password(u):
    global username
    username=u


    def updt(curp,nep,cnep):
        global username
        if curp!="" and nep!="" and cnep!="":
            cursor.execute("SELECT password from users WHERE username =?",[u])
            if cnep!=curp:
                if nep==cnep:
                    a=cursor.fetchone()
                    if a[0]==curp:
                        cursor.execute("UPDATE users SET password=? WHERE username=?",[cnep,u])
                        link.commit()
                        root.destroy()
                        messagebox.showinfo("Success","Password updated successfully")
                    else:
                        messagebox.showerror("Credential Error","Password incorrect")
                        cnewpass.delete(0,END)
                        newpass.delete(0,END)
                        oldpass.delete(0,END)
                else:
                        messagebox.showwarning("Warning!","Passwords must be same")
                        cnewpass.delete(0,END)
                        newpass.delete(0,END)
            else:
                    messagebox.showwarning("Warning!","Old Password And New Password Cannot be same")

                    cnewpass.delete(0,END)
                    newpass.delete(0,END)
                    oldpass.delete(0,END)
        else:
            messagebox.showwarning("Warning!","All Fields must be filled")
        root.deiconify()
    
    def kensil():
        root.destroy()

    root=Tk()
    root.geometry('500x350')
    root.resizable(False,False)
    root.title('Settings')
    root.iconbitmap("assets/main.ico")  
    main=Frame(root,width=500, height=350)
    main.config(bg="#5585b5")
    main.place(x=0,y=0)
    a=Frame(main,height=60,width=480,bg="#bbe4e9")
    a.place(x=10,y=10)

    labe=Label(a,text="Reset Password",font=('Helvetica', 30),bg="#bbe4e9")
    labe.place(anchor="center",relx=0.5,rely=0.5)
    Mfrm=Frame(main,width=480, height=200,bg="#53a8b6")
    Mfrm.place(relx=0.5,rely=0.5,anchor="center")
    


    
    a=Label(Mfrm,text="Current Password:",font=('Helvetica', 20),bg="#53a8b6")
    a.place(x=10,y=20)
    oldpass=Entry(Mfrm,font=('Helvetica', 20),show="*",width=15)
    oldpass.place(x=240,y=15)

    b=Label(Mfrm,text="New Password    :",font=('Helvetica', 20),bg="#53a8b6")
    b.place(x=12,y=90)
    newpass=Entry(Mfrm,font=('Helvetica', 20),show="*",width=15)
    newpass.place(x=240,y=90)

    b2=Label(Mfrm,text="Confirm Password:",font=('Helvetica', 20),bg="#53a8b6")
    b2.place(x=12,y=150)
    cnewpass=Entry(Mfrm,font=('Helvetica', 20),show="*",width=15)
    cnewpass.place(x=240,y=150)
    
    Button(main,text="Cancel",command=lambda :kensil(), font=('Helvetica', 20),bg="#bbe4e9",width=15,height=1).place(x=240,y=280)
    Button(main,text="Submit",command=lambda: updt(oldpass.get(),newpass.get(),cnewpass.get()), font=('Helvetica', 20),bg="#bbe4e9",width=15,height=1).place(x=10,y=280)

    root.mainloop() 
    

def render(username,function):
    
    

     if function=="rpass":
          password(username)


global FName,phone,address,Title_,Checkbutton1,Checkbutton2,Checkbutton3         

def adddata(u):
    def submit(u):
        def gendergrab():
            if (Checkbutton1.get())==1:
                gender="M"
            elif Checkbutton1.get()==2:
                gender="F"
            elif Checkbutton1.get()==3:
                gender="O"
            else:
                gender="EROOR"
            return gender
        hal(u,FName.get(),gendergrab(),phone.get(),address.get(),Title_.get(),1)
        root2.destroy()
    global root
    root2=Tk()
    root2.geometry('800x800')
    root2.resizable(False,False)
    root2.title('Data add')
    root2.iconbitmap("assets/main.ico")  
    main=Frame(root2,width=800, height=800)
    main.config(bg="#5585b5")
    main.place(x=0,y=0)

    #Title
    Title_Frame=Frame(main,height=60,width=750,bg="#bbe4e9")
    Title_Frame.place(relx=0.5,rely=0.05,anchor="center")
    Title_Txt=Label(Title_Frame,text="Create ID card- Please Fill the Details",font=(('Helvetica', 30)),bg="#bbe4e9")
    Title_Txt.place(relx=0.5,rely=0.5,anchor="center")

    #Form
    Form_Frame=Frame(main,height=600,width=750,bg="#bbe4e9")
    #Form-Labels
    Form_Frame.place(relx=0.5,rely=0.5,anchor="center")
    Form_Txt0=Label(Form_Frame,text="the fields marked with * are mandatory to fill",font=(('Helvetica',20)),fg="orange",bg="#515A5A")
    Form_Txt0.place(relx=0.5,rely=0.05,anchor="center")
    Form_Txt=Label(Form_Frame,text="* Full Name:",font=(('Helvetica', 25)),bg="#839192")
    Form_Txt.place(relx=0.15,rely=0.22,anchor="center")
    Form_Txt1=Label(Form_Frame,text="* Gender:",font=(('Helvetica', 25)),bg="#839192")
    Form_Txt1.place(relx=0.13,rely=0.33,anchor="center")
    Form_Txt2=Label(Form_Frame,text="* Phone Number:",font=(('Helvetica', 25)),bg="#839192")
    Form_Txt2.place(relx=0.205,rely=0.44,anchor="center")
    Form_Txt3=Label(Form_Frame,text="* Address:",font=(('Helvetica', 25)),bg="#839192")
    Form_Txt3.place(relx=0.145,rely=0.55,anchor="center")
    Form_Txt4=Label(Form_Frame,text="Company name/Title:",font=(('Helvetica', 25)),bg="#839192")
    Form_Txt4.place(relx=0.25,rely=0.66,anchor="center")
    Form_Txt5=Label(Form_Frame,text="Profile Picture: \n (If empty, Profile \naccording to gender)",font=(('Helvetica', 25)),bg="white")
    Form_Txt5.place(relx=0.25,rely=0.85,anchor="center")
    k22=Label(Form_Frame,text="Selected image =None",font=('Helvetica',8))
    k22.place(relx=0.7,rely=0.77,anchor="center")
    
    
    global FName,phone,address,Title_,Checkbutton1,Checkbutton2,Checkbutton3 
    #Form-Entries
    FName=Entry(Form_Frame,width=25,font=('Helvetica',25))
    FName.place(relx=0.3,rely=0.185)
    phone=Entry(Form_Frame,width=20,font=('Helvetica',25))
    phone.place(relx=0.4,rely=0.405)
    address=Entry(Form_Frame,width=25,font=('Helvetica',25))
    address.place(relx=0.27,rely=0.515)
    Title_=Entry(Form_Frame,width=20,font=('Helvetica',25))
    Title_.place(relx=0.48,rely=0.627)

    #Form-Gender selector
    Checkbutton1 = IntVar()   
    Button1 = Radiobutton(Form_Frame, text = "Male",  
                        variable = Checkbutton1, 
                        value=1,
                        height = 2, 
                        width = 10) 
    
    Button2 = Radiobutton(Form_Frame, text = "Female", 
                        variable = Checkbutton1, 
                        value=2,
                        height = 2, 
                        width = 10) 
    
    Button3 = Radiobutton(Form_Frame, text = "Others", 
                        variable = Checkbutton1, 
                        value=3,
                        height = 2, 
                        width = 10)   
        
    Button1.place(relx=0.33,rely=0.33,anchor="center")   
    Button2.place(relx=0.53,rely=0.33,anchor="center")   
    Button3.place(relx=0.73,rely=0.33,anchor="center")


    
    select_img= Button(Form_Frame,text="Select Image",font=('Helvetica',20))
    select_img.place(relx=0.6,rely=0.9,anchor="center")

    #buttons
    intrx_Frame=Frame(main,height=70,width=750,bg="#bbe4e9")
    intrx_Frame.place(relx=0.5,rely=0.94,anchor="center")
    def bhak():
        root2.destroy()
        return u
    intrx_ext=Button(intrx_Frame,text="Cancel",font=(('Helvetica', 23)),width=19,bg="GREY",command=bhak)
    intrx_ext.place(relx=0.75,rely=0.5,anchor="center")
    intrx_sbt=Button(intrx_Frame,text="Submit",font=(('Helvetica', 23)),width=20,bg="GREY",command=lambda: submit(u))
    intrx_sbt.place(relx=0.26,rely=0.5,anchor="center")
    root2.mainloop()
    print("baira gao")
    return u

     

