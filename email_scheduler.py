import sqlite3
from tkinter import *
import sched
import smtplib
import easygui
from threading import Timer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from datetime import datetime


conn = sqlite3.connect('./mails.db')
c = conn.cursor()

msg = MIMEMultipart()

threads=[]

root=Tk()           ## Login Frame
root.wm_title("E-mail Scheduler")
root.withdraw()

sel=Tk()            ## Select Frame
sel.wm_title("E-mail Scheduler")
sel.withdraw()

reg=Tk()            ## Register frame
reg.wm_title("E-mail Scheduler")
reg.withdraw()

start=Tk()          ## Send Mail

start.wm_title("E-mail Scheduler")
start.withdraw()

c.execute('select count(id) from mails')
index=c.fetchall()
index=index[0][0] + 1


l1,l2=1,0

def create_tables_mail():
    c.execute("CREATE TABLE IF NOT EXISTS mails(id INTEGER,timer TEXT, rec_mail TEXT ,sub TEXT,body TEXT,attachment TEXT,status INTEGER)")


def data_entry_mail(t1,r1,s1,b1,a1):
    global index
    c.execute("INSERT INTO mails (id,timer,rec_mail,sub,body,attachment) VALUES(?,?,?,?,?,?)",
              (index,t1,r1,s1,b1,a1))
    
    index=index+1
    conn.commit()
    


def create_tables():
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY,name TEXT,email TEXT, Mobile TEXT,company TEXT,password TEXT,confirm TEXT)")


def data_entry(u1,n1,email,mob,comp,password,cnf_password):
    
    c.execute("INSERT INTO users (username,name,email, Mobile,company,password,Confirm) VALUES(?,?,?,?,?,?,?)",
              (u1,n1,email,mob,comp,password,cnf_password))

    conn.commit()

def pop_up(msg,no):  # to show pop up about details saved
    conn1=sqlite3.connect('./mails.db')
    c1=conn1.cursor()
    
    no=int(no)
    if msg == 'Mail Sent Successfully':
        c1.execute(" Update mails set status = 1 where id= ? ",
                   (no,))
        conn1.commit()
        c1.close()
    else:
        c1.execute(" Update mails set status = 0 where id= ? ",
                   (no,))
        conn1.commit()
        c1.close()

    NORM_FONT = ("Helvetica", 10)
    popup=Tk()
    popup.wm_title("E-mail Scheduler")
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)

    B1 = Button(popup, text="Exit", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
    conn1.close()

def main_mail(idf=None):
    start.deiconify()
    def attach():
        file = easygui.fileopenbox()
        t2.insert(10,file)
        attachment=open(file,'rb')
        filename=os.path.basename(file)
        p=MIMEBase('application','octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        attachment.close()

    v1=StringVar(start)
    v2=StringVar(start)
    v3=StringVar(start)
    v5=StringVar(start)

    t1=Text(start,width=75,height=20)            # Body
    t2=Entry(start,width=80,textvariable=v5)     # attach

    start.wm_title('E-mail Scheduler')
    Label(start,text="To").grid(row=2,sticky="W")
    Label(start,text="Subject").grid(row=3,sticky="W")
    Label(start,text="Body").grid(row=4,sticky="WN")
    Label(start,text="Attach").grid(row=5,sticky="WN")
    Label(start,text="Date and Time").grid(row=6 )
    Label(start,text='''(Format for the input is YYYY-MM-HH HH:MM Time is in 24 hour format
             Eg: '2018-09-10 18:02' for 10 september 2018 06:02 pm excluding single quotes)''').grid(row=7,column=2)



    t2.grid(row=5,column=2,padx=2,pady=2,sticky="W")            # For attachment
    Button(start, text="Select",command=attach).grid(row=5,column=2,sticky="E")

    t3=Entry(start,width=100,textvariable=v1)
    t3.grid(row=2,column=2,padx=2,pady=2)                       # To reiever's mail address

    t4=Entry(start,width=100,textvariable=v2)
    t4.grid(row=3,column=2,padx=2,pady=2)                       # Subject

    t1.grid(row=4,column=2,padx=2,pady=2)                       # Body

    e3=Entry(start,width=100,textvariable=v3)
    e3.grid(row=6,column=2,padx=2,pady=2)                       # time and date


    if(idf=='0'):
        placeholder=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        e3.insert(10,placeholder)

    elif(idf):
        c.execute('Select * from mails where id=? ',idf)
        data=c.fetchall()
        for j in data:
            t2.insert(0,j[5])
            t1.insert(END, j[4] )
            t4.insert(0,j[3])
            t3.insert(0,j[2])
            e3.insert(0,j[1])


    def wipe():
        start.withdraw()
        select()

    

    def timer():

        def send_mail(no , rec_mail , sub , body):
        
            sender_mail="milloionmoney@gmail.com"

            msg["From"]=sender_mail
            msg["To"]=",".join(rec_mail)
            msg["Subject"]=sub
            
            msg.attach(MIMEText(body,'plain'))

            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login("milloionmoney@gmail.com","8572090630")
            try:
                server.sendmail(sender_mail,rec_mail,msg.as_string())
                pop_up('Mail Sent Successfully',no)
            except:
                pop_up('Unable to Send Mail',no)
            finally:
                server.quit()
                

        
        print('enter timer')
        start.withdraw()
        today = datetime.today()
        c.execute("SELECT * from mails")
        data=c.fetchall()
        print('data get')
        print(data)

        for s in data:
            if s[6]!=1:
                
                enter_date=datetime.strptime(s[1].split(".")[0],'%Y-%m-%d %H:%M:%S')
                print(enter_date,today)
                if enter_date<today:
                    diff=1
                else:
                    diff = (enter_date - today).seconds
                print(diff)
                rec_mail=list(s[2].split(','))
                t1=Timer( diff ,send_mail,(s[0],rec_mail,s[3],s[4]))
                t1.start()
            else:
                pass
        select()
    def store():
        mails=v1.get()
        sub=v2.get()
        time=v3.get()
        attach=v5.get()
        body=t1.get("1.0","end-1c")
        print(time,mails,sub,body,attach)
        time=datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
        data_entry_mail(time,mails,sub,body,attach)
        print('data saved')
        timer()


    Button(start, text="Submit",command=store).grid(row=12,column=2,padx=20,pady=2)
    Button(start, text="Exit",command=wipe).grid(row=12,column=2,padx=20,sticky="E")
    mainloop()
    
    
def select():
    sel.deiconify()
    c.execute("SELECT * from mails")
    data=c.fetchall()

    Label(sel,text='S No').grid(row=1)
    Label(sel,text='Date And Time').grid(row=1,column=1,padx='30')
    Label(sel,text='Subject').grid(row=1,column=2,padx='30')
    Label(sel,text='Recieptent').grid(row=1,column=3,padx='30')

    def sen_mail(idf):
        sel.withdraw()
        idf=str(idf)
        main_mail(idf)
    
    Button(sel,text='Schedule New',command=lambda:sen_mail(0)).grid(row=1,column=4)
    k=2

    def ting():
        conn.close()
        start.destroy()
        reg.destroy()
        sel.destroy()
        sys.exit(0)
    Button(sel,text='Exit',command=lambda:ting()).grid(row=k+2,column=2)

    for s in data:
        
        if s[6]!=1:
            idf=s[0]
            
            mail=''
            datetime=s[1]
            sub=s[3]
            mails=s[2]

            Label(sel,text=k).grid(row=k)
            Label(sel,text=datetime).grid(row=k,column=1,padx='30')
            Label(sel,text=sub).grid(row=k,column=2,padx='30')
            Label(sel,text=mails).grid(row=k,column=3,padx='30')

            
            Button(sel,text='Edit',command=lambda:sen_mail(idf)).grid(row=k,column=4)
            mainloop()
            k+=1

def frame():  # for register frame
    reg.deiconify()
    
    Label(reg,text='Username').grid(row=0,sticky='w')
    Label(reg,text='Name* ').grid(row=1,sticky='w')
    Label(reg,text='Email*').grid(row=2,sticky='w')
    Label(reg,text='Mobile Number* ').grid(row=3,sticky='w')
    Label(reg,text='Company Name ').grid(row=5,sticky='w')
    Label(reg,text='Password* ').grid(row=6,sticky='w')
    Label(reg,text='Confirm Password* ').grid(row=7,sticky='w')

    d0=Entry(reg,width='35')
    d0.grid(row=0,column=1)

    d1=Entry(reg,width='35')
    d1.grid(row=1,column=1) # Name

    d2=Entry(reg,width='35')
    d2.grid(row=2,column=1) # Email 

    d3=Entry(reg,width='35')
    d3.grid(row=3,column=1) # Mobile Number

    d4=Entry(reg,width='35')
    d4.grid(row=5,column=1) # Company name

    d5=Entry(reg,show='*',width='35')
    d5.grid(row=6,column=1) # Password

    d6=Entry(reg,show='*',width='35')
    d6.grid(row=7,column=1) # Confirm password


    def save_details():  # to store data in db
       # (n1,e1,comp_1,mob_1,pass_1,cnf_pass_1)=('1','1','1','1','1','1')

        u1=d0.get()
        n1=d1.get()         # Name
        e1=d2.get()
        c1=d4.get()         #Comapny Name
        m1=d3.get()         # mobile number
        try:
            m1=int(m1)
        except:
            Label(reg,text='Please Enter Numbers only').grid(row=4,column=1)
            return
            
        p1=d5.get()
        cp1=d6.get()

        if p1!=cp1:
            Label(reg,text="Please Enter Same password ").grid(row=8,column=1)
            return
        print(u1,n1,e1,m1,c1,p1,cp1)
        data_entry(u1,n1,e1,m1,c1,p1,cp1)
        reg.withdraw()
        pop_up('Details Saved')
        reg.withdraw()
        login()

    def back():
        reg.withdraw()
        login()


    Button(reg,text='Sign Up',command=save_details).grid(row=10,column=1,padx=20,sticky='w')

    Button(reg,text=' Cancel ',command=back).grid(row=10,column=1,padx=20,sticky='e')

    reg.mainloop()

    
def login():
    root.deiconify()
    v1=StringVar()
    v2=StringVar()
    Label(root,text="Username").grid(row=0)
    Label(root,text="Password").grid(row=1)
    
    Entry(root,textvariable=v1,width="35").grid(row=0,column=1)
    Entry(root,textvariable=v2,width="35",show="*").grid(row=1,column=1)

    def check():
        c.execute("SELECT username,password from users")
        for s in c.fetchall():
            if v1.get()==s[0]:
                if v2.get()==s[1]:
                    root.withdraw()
                    select()
                else:
                    Label(root,text="Username and Password Combination not matched").grid(row=3,column=1)

    def regis():
        root.withdraw()
        frame()
        
    Button(root, text="Log In",command=check).grid(row=4,column=1,padx="40",sticky="w")
    Button(root, text="Register ",command=regis).grid(row=4,column=1,padx="40",sticky="e")

    mainloop()


create_tables()
create_tables_mail()
login()
