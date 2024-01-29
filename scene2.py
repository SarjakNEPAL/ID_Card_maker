from condata import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import settings
import io



global con 

global app2


con=""


def start(a):
    global con 
    global app2
    app2=Tk()
    def ext():
        link.close()
        app2.destroy()
           
    def logout():
        global con
        con='Logout'
        app2.destroy()
    
    

    global data 
    data=a
    app2.title("ID generator")
    app2.iconbitmap("assets/main.ico") 
    app2.geometry("1000x500")
    app2.resizable(False,False)
    
    #frames
    main=Frame(app2, height="500", width="1000",bg="#515A5A")
    main.pack()

    frame2=Frame(main, height="500",width="300",bg="#839192")
    frame2.place(x="0",y="0")
    frame21=Frame(frame2, height="180",width="280",bg="#2E4053")
    frame21.place(x=10,y=200)
    frame22=Frame(frame2, height="50",width="280",bg="#D6DBDF")
    frame22.place(x=10,y=130)
    frame23=Frame(frame2, height="50",width="280",bg="#BFC9CA")
    frame23.place(x=10,y=10)
    frame24=Frame(main, height=460,width=660,bg="#BFC9CA")
    frame24.place(x=320,y=20)

    def setti():
        settings.render(a,"rpass")

    
    #buttons
    b=Button(frame2,text="Exit",height=4, width=40,bg="#BFC9CA",command=ext)
    b.place(x=5,y=400)
    b1=Button(frame21,text="Settings",height=4, width=36,bg="#BFC9CA",command=lambda: setti())
    b1.place(x=10,y=10)
    b2=Button(frame21,text="Logout",height=4, width=36,bg="#BFC9CA",command=logout)
    b2.place(x=10,y=100)
     #labels
    k=Label(frame22,text=f"User: {a}",bg="#BFC9CA",font=("Small Font",25))
    k.place(x=1,y=1)
    k1=Label(frame23,text="DASHBOARD",bg="#BFC9CA",font=("Small Font",25))
    k1.place(x=23,y=5)

    # Load the image from the provided path
    
    def dataexist(a):
        cursor.execute('SELECT username FROM user_info where username=?',[a])
        d=cursor.fetchone()
        if d!=None: return True
        else:False
    
    def datasend(a):
        if dataexist(a):
            messagebox.showerror("Error","data already exists")
        else:
            app2.destroy()
            if (settings.adddata(a))==a:
                print("aayo")
                start(a)
    

    if(dataexist(a)):
        import maker
        template_path = "assets/template1.png"
        img = Image.open(template_path)
        tempimg = ImageTk.PhotoImage(img.resize((660, 460)))
        Fullname=Label(frame24,text="Sample text1",font=('Sans',20))
        Fullname.place(x=50,y=50)
        # Display the image in a label within the MainFrame
        template_label =Label(frame24, image=tempimg)
        template_label.pack(expand=True, fill='both', anchor='center')


        #adding info in the canvas
        datas= maker.fetchgar(a)
        #Labels
        Fullname=Label(frame24, text=f"{datas[0]}",font=("Sans",20),bg="White")
        Fullname.place(x=355,y=150)
        if datas[1]=="M":
            Gender=Label(frame24, text="Gender: Male",font=("Sans",20),bg="White")    
        elif datas[1]=="F":
            Gender=Label(frame24, text="Gender: Female",font=("Sans",20),bg="white")     
        else:
            Gender=Label(frame24, text="Gender: LGBTQ+",font=("Sans",20),bg="White")
        Gender.place(x=255,y=260)      
        num=Label(frame24, text=f"{datas[2]}",font=("Sans",20),bg="White")  
        num.place(x=360,y=225)
        address=Label(frame24, text=f"{datas[3]}",font=("Sans",20),bg="White")  
        address.place(x=378,y=185)
        company=Label(frame24, text=f"{datas[4]}",font=("Terminal",25),bg="Orange") 
        company.place(relx=0.5,rely=0.25,anchor="center")

        #profile picture
        pfp_frame=Frame(frame24,height=150,width=150,bg="green")
        pfp_frame.place(x=95,y=152)

        if maker.chapic(a):
            cursor.execute('''SELECT Image FROM user_img where username=?''',[a])
            d=cursor.fetchone()[0]
            dato=io.BytesIO(d)
            image=Image.open(dato)
        else: 
            if datas[1]=='M':
                loca='assets/man.png'
                pfp_frame.config(bg="#D1D1D3")
            elif data[1]=="F":
                loca='assets/woman.png'
                pfp_frame.config(bg="#4C5AA5")
            else:
                loca='assets/lgbtq.png'
                pfp_frame.config(bg="#4C5AA5")
            image=Image.open(loca)
        pfp_pic=ImageTk.PhotoImage(image.resize((150,150)))
        pfp_Label=Label(pfp_frame,image=pfp_pic)
        pfp_Label.pack()
    
            
        



    else:
        bu=Button(frame24,text="Create",command=lambda:datasend(a))
        bu.place(relx=0.5,rely=0.5,anchor="center")
    app2.mainloop()

    return con


if __name__ == "__main__":

    start('Sarjak')