from condata import *
from tkinter import *
import settings



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
        link.close()
        global con
        con='Logout'
        ext()
    
    

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
    app2.mainloop()
    return con

if __name__ == "__main__":
    start('sar')