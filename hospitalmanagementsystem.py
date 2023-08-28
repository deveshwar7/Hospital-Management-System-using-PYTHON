from tkinter import *
from tkinter import messagebox



t=Tk()
t.configure(background="#C2DFFF")


my_image=PhotoImage(file='C:\\Users\\HP\\OneDrive\\Pictures\\Firstpage.png')
label1=Label(image=my_image)
label1.place(x=500,y=190)






p=StringVar()
q=StringVar()
e1=StringVar()
e2=StringVar()

def pp():
 m=Tk()
 p=StringVar()
 q=StringVar()
 m.title("LOGIN SYSTEM")
 m.geometry("1500x1500")


 bordercolor=Frame(m,bg='black',width=800,height=550)
 bordercolor.place(x=600,y=100)
 mainframe=Frame(bordercolor,bg='lightcyan',width=800,height=550)
 mainframe.pack(padx=15,pady=15)




 m.configure(background="mistyrose")
 
 l1=Label(m,text="LOGIN DETAILS",fg="white",bg='#4b0082',font=('broadway',24,'bold','underline'))
 l1.place(x=900,y=150)
 l2=Label(m,text="Enter your Username",fg="white",bg='#0000FF',font=('arial',15,'bold')).place(x=800,y=250)
 e1=Entry(m ,textvariable=p).place(x=1050,y=250)
 l3=Label(m,text="Enter your Password",fg="white",bg='#34A56F',font=('arial',15,'bold')).place(x=800,y=350)
 e2=Entry(m,show="*",textvariable=q).place(x=1050,y=350)
 b=Button(m,text="Click here for Login",height="2",width=22,command=login1,fg="white",bg="#ed3833",font=('arial',10,'bold')).place(x=700,y=500)
 b=Button(m,text="Reset",fg="white",height="2",width=22,bg="#C35817",font=('arial',10,'bold')).place(x=900,y=500)
 b=Button(m,text="Exit",fg="white",height="2",width=22,bg="#FFA500",font=('arial',10,'bold')).place(x=1100,y=500)


def login():
    username=e1.get()
    password=e2.get()
    b=Button(text="Login",command=login)
    n="abc"
    m="1234"
#print("You are Logged in")

def add():
        o=Tk()
        o.title("Supplier Information")
        o.geometry("1500x1500")
        bordercolor=Frame(o,bg='black',width=800,height=550)
        bordercolor.place(x=600,y=100)
        mainframe=Frame(bordercolor,bg='lightcyan',width=800,height=550)
        mainframe.pack(padx=15,pady=15)
        o.configure(background="#FAEBD7")
        d1=Label(o,text="Add Suppliers",fg="white",bg='#4b0082',font=('broadway',24,'bold','underline'),)
        d1.place(x=900,y=150)
        d2=Label(o,text="Enter new Suppliers",fg="white",bg='#0000FF',font=('arial',15,'bold')).place(x=800,y=250)
        e1=Entry(o ,textvariable=p).place(x=1050,y=250)
        fy=Label(o,text="Enter gggggg name",fg="white",bg='#0000FF',font=('arial',15,'bold')).place(x=900,y=450)
def logp():

  pp()

def login1():
    
    
     pm=Tk()
      
     pm.title("DASHBOARD")
     pm.geometry("1500x1500")
     #pm.configure(background="#B4CFEC")
     menubar=Menu(pm)
     Supp=Menu(menubar,tearoff=0)
     menubar.add_cascade(label='Suppliers',menu=Supp)
     Supp.add_command(label='Add Supplier',command=add)
     
     dist=Menu(menubar,tearoff=0)
     menubar.add_cascade(label='Distributors',menu=dist)
     dist.add_command(label='Add Distributor')
     
     gov=Menu(menubar,tearoff=0)
     menubar.add_cascade(label='Government Hospitals',menu=gov)
     gov.add_command(label='Add Government Hospitals')
    
     pri=Menu(menubar,tearoff=0)
     menubar.add_cascade(label='Private Hospitals',menu=pri)
     pri.add_command(label='Add Private Hospitals')
     
     sur=Menu(menubar,tearoff=0)
     menubar.add_cascade(label='Surgical Stores',menu=sur)
     sur.add_command(label='Add Surgical Stores')

     rep=Menu(menubar,tearoff=0)
     menubar.add_cascade(label='Report',menu=rep)
     rep.add_command(label='Click Here for Reports')

     log=Menu(menubar,tearoff=0)
     menubar.add_cascade(label='Logout',menu=log)
     log.add_command(label='Click Here to Log Out!',command=logp)
     
     pm.config(menu=menubar)

    
      #print("You can exit")
 

     







t.title("CASTLE BLANCE MEDICAL SYSTEM")

l1=Label(t,text="WELCOME TO MY MEDICAL AGENCY SYSTEM",bd=10,relief=RIDGE,fg="white",bg="#DA70D6",font=('Times New Roman',24,'bold','underline')).pack(side=TOP,fill=X)
t.geometry("1500x1500")
l2=Label(t,text= "A Transforming, Healing Presence" ,fg="#FF7722",font=('Elephant',20,'italic','bold')).place(x=500,y=80)
l3=Label(t,text="     My healthcare agency system is used in an allied health professional areas who supports the work of physicians, nurse practitioners,\n assistants and other health professionals,usually in a clinic or hospital setting. \n This system helps in performing routine tasks and procedures in a medical domain!",fg="#B048B5",font=('Times New Roman',15,'italic'))
l3.place(x=180,y=450)
b=Button(t,text="CLICK HERE FOR LOGIN DETAILS",fg="white",bg="#F67280",font=('Times New Roman',10,'bold'),command=pp).place(x=680,y=600)


