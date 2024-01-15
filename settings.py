from tkinter import *
from condata import *
from tkinter import messagebox


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
        else:
            messagebox.showwarning("Warning!","All Fields must be filled")
    
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
     





if __name__=='__main__':
    render("Sarjak","rpass")


