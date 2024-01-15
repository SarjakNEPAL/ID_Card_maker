import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from condata import *

global username
global password

def render(kkggv):
    global isok, app, username
    app=tk.Tk()
    isok=False
    if kkggv == True:
        app.title("ID generator")
        app.iconbitmap("assets/main.ico") 
        app.geometry("1000x500")
        app.resizable(False,False)

        def dataget():
            global username
            username=user1.get()                
            cursor.execute('SELECT password FROM users WHERE username=?',[username])
            re=cursor.fetchone()
            return re
            
        def lg():
            subtitle.config(text="Login")
            Bttn2.config(text="Register", command=reg)
            Bttn.config(text="Login",command=checkfld)

        def lgmn(u,p):
            global isok
            isok=False
            a=dataget()
            cursor.execute('SELECT username FROM users WHERE username=?',[username])
            if a is not None and p != '' and a[0] == p:
                print(a)
                isok=True
                app.destroy()
            else:
                messagebox.showerror("CREDENTIAL ERROR","Username or Password error")
                isok=False
            pass1.delete(0,END)

        def signup():
            username=user1.get()
            password=pass1.get()
            print(username,password)
            if username !='':
                if password!='' and len(password)>7:
                    cursor.execute('SELECT username FROM users WHERE username=?',[username])
                    if cursor.fetchone() is not None:
                        messagebox.showerror('Error',"Username already exists")
                    else:
                        cursor.execute('INSERT INTO users VALUES(?,?)',[username,password])
                        link.commit()

                        messagebox.showinfo('Success',"Account has been created")         
                        lg()       
                else:
                    messagebox.showwarning("Password error","Password must contain more than 7 characters")
            else:
                messagebox.showwarning("Warning!","Username must not be blank")
            user1.delete(0,END)
            pass1.delete(0,END)
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
        # Open the image
        image_path = 'assets/id-card.png'  # Provide the correct path to your image
        Ad_img = Image.open(image_path)

        # Create a PhotoImage object
        ad_pic = ImageTk.PhotoImage(Ad_img.resize((400, 440)))

        # Display the image on a label
        adlabel = ttk.Label(Ad, image=ad_pic, background='#79c2d0')
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
            global username
            global password
            username=user1.get()
            password=pass1.get()
            if username !='':
                if password!='' and len(password)>7:
                    lgmn(username,password)
                else:
                    messagebox.showwarning("Password error","Password must contain more than 7 characters")
            else:
                messagebox.showwarning("Warning!","Username must not be blank")

        
        def reg():
            subtitle.config(text="Register")
            Bttn.config(text="Register", command=signup)
            Bttn2.config(text="Login",command=lg)

        #Default entries
        crtr=Label(creator,text="|||| Created By - Sarjak Bhandari ||||",font=('Helvetica', 20),bg="#bbe4e9")
        usrnmr_=Label(Mfrm,text="Username:",font=('Helvetica', 25),bg="#53a8b6")
        pss_=Label(Mfrm,text="Password:",font=('Helvetica', 25),bg="#53a8b6")
        Bttn=Button(Mfrm,text="Login",bg="#ececec",height=1,width=10,font=('Helvetica', 20),command=checkfld)
        Bttn2=Button(Mfrm,text="Register",bg="#ececec",height=1,width=10,font=('Helvetica', 20),command=reg)
        Button(main,text="Exit",command=ext,font=('Helvetica', 20),bg="#bbe4e9",width=30,height=1).place(x=455,y=380)
        #inputs
        user1=Entry(Mfrm,font=('Helvetica', 20))
        pass1=Entry(Mfrm,font=('Helvetica', 20),show="*")
        crtr.place(x=40,y=5)
        usrnmr_.place(x=20,y=10)
        pss_.place(x=20,y=70)
        Bttn.place(x=50,y=130)
        Bttn2.place(x=250,y=130)
        user1.place(x=185,y=15)
        pass1.place(x=185,y=75)
        #login function
        app.mainloop()
    elif isok==False or kkggv==False:
        app=Tk()
        app.destroy()
    return isok

def getuname():
    return username

    
    