from ast import Sub
from tkinter import *
from tkinter import messagebox
from tkinter import font
import FirebaseDB
from PIL import ImageTk, Image
import EmailReciverExtra 
import os
import PDFprocessor


login_screen=None
def loginScreen():
    login_screen=Tk()
    login_screen.title('CDR-login')
    login_screen.geometry('950x520+300+200')
    login_screen.configure(bg='#fff')
    login_screen.resizable(False,False)
    Bg_img=ImageTk.PhotoImage(Image.open('images/My_Login.png'))
    img_label=Label(login_screen,image=Bg_img,bg='white').place(x=50,y=50)
    frame=Frame(login_screen,width=350,height=350,bg='white')

    frame.place(x=480,y=70)
    fnt=('Microsft YaHei UI Light',25)
    heading=Label(frame,text="Sign in" ,font=fnt,bg='white',fg='#57a1f8').place(x=100,y=5)

    ##################################################
    def on_enter(e):
        Email_add.delete(0,'end')

    def on_leave(e):
        name=Email_add.get()
        if name=='':
            Email_add.insert(0,'Email')
    Email_add=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
    Email_add.place(x=30,y=80)
    Email_add.insert(0,'Email')
    Email_add.bind('<FocusIn>',on_enter)
    Email_add.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=104)
    ##################################################
    def on_enter(e):
        password.delete(0,'end')

    def on_leave(e):
        name=password.get()
        if name =='':
            password.insert(0,'Password')
    password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
    password.place(x=30,y=150)
    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    password.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=174)
    ##################################################
   
    Login_btn=Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0,command=lambda:validation_login(email=Email_add.get(),password=password.get(),root=login_screen)).place(x=35,y=204)
    Label(frame,text="Don't have an account?",fg='black',bg='white',font= ('Microsft YaHei UI Light',9)).place(x=35,y=270)
    Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=lambda: Register_Screen(login_screen)).place(x=180,y=270)




    login_screen.mainloop()






def validation_login(email,password,root):
    if email is not None:
        user_info=FirebaseDB.database.child('Users').child(str(email.split('@')[0])).get()
        if user_info is None:
            messagebox.showerror('Invaild' ,'Wrong Email or password!')
        else:
                print(user_info.val())
                if user_info.val()['password']==password:
                    print('ok')
                    CDR_Mail_form(mail=email,password=user_info.val()['App'],root=root)
                else:
                    messagebox.showerror('Invaild','incorrect password!')
    else:
        messagebox.showerror('Invaild','Enter email!!')



def Register_Screen(root):
    register_screen=Toplevel(root)
    register_screen.title('CDR-sign up')
    register_screen.geometry('950x520+300+200')
    register_screen.configure(bg='#fff')
    register_screen.resizable(False,False)
    img=ImageTk.PhotoImage(Image.open('images/My_Login.png'))
    Label(register_screen,image=img,border=0,bg='white').place(x=50 ,y=50)
    frame=Frame(register_screen,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    fnt=('Microsft YaHei UI Light',25)
    heading=Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=fnt)
    heading.place(x=100,y=5)


    ##################################################
    def on_enter(e):
        Email.delete(0,'end')

    def on_leave(e):
        name=Email.get()
        if name=='':
            Email.insert(0,'Email')
    Email=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
    Email.place(x=30,y=80)
    Email.insert(0,'Email')
    Email.bind('<FocusIn>',on_enter)
    Email.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=104)
    ##################################################
    def on_enter(e):
        password.delete(0,'end')

    def on_leave(e):
        name=password.get()
        if name =='':
            password.insert(0,'Password')
    password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
    password.place(x=30,y=150)
    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    password.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=174)
    ################################################## 
    def on_enter(e):
         App_password.delete(0,'end')
    def on_leave(e):
        name=App_password.get()
        if name =='':
            App_password.insert(0,'App Password')
    App_password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
    App_password.place(x=30,y=220)
    App_password.insert(0,'App Password')
    App_password.bind('<FocusIn>',on_enter)
    App_password.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
    #####################################################
    def signup():
        all_users=FirebaseDB.database.child('Users').get()
        if (Email.get()=='' or Email.get()=='Email') and ( password.get()=='' or password.get()=='Password') and (App_password.get()=='' or App_password.get()=='App Password'):
            messagebox.showerror('Invaild','please enter data...')
        elif Email.get()=='' or Email.get()=='Email':
            messagebox.showerror('Invaild','Enter email!!!!')
        elif password.get()=='' or password.get()=='Password':
            messagebox.showerror('Invaild','enter your password')
        elif App_password.get()=='' or App_password.get()=='App Password':
            messagebox.showerror('Invaild','enter the app password of your mail!!')
        elif Email.get()!='' and password.get()!='' and App_password.get()!='':
            check_mail=False
            for user in all_users.each():
                key_comp=str(user.key()+'@gmail.com')
                if key_comp==Email.get():
                    check_mail=True
                    messagebox.showerror('Invaild','this email already have account')
            if check_mail==False:
                data={'App':App_password.get(),'Email':Email.get(),'password':password.get()}
                key_add=Email.get().split('@')[0]
                FirebaseDB.database.child('Users').child(str(key_add)).set(data=data)
                messagebox.showinfo('SignUp','Successfully sign up')
            
    signup_btn=Button(frame,width=39,pady=7,text='Sign up', bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    Label(frame,text="have an account?",fg='black',bg='white',font= ('Microsft YaHei UI Light',9)).place(x=75,y=335)
    Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=loginScreen).place(x=180,y=335)
    register_screen.mainloop()



# email_address,password
def CDR_Mail_form(mail,password,root):
   frm=Toplevel(root)
   frm.geometry('950x520+300+200')
   frm.title('CDR')
   frm.configure(bg='#fff')
   frm.resizable(True,True)
   main_frame=Frame(frm,width=80,height=frm.winfo_screenheight(),bg='#A9A9A9')
   main_frame.place(x=0,y=0)
   icon=ImageTk.PhotoImage(Image.open('images/My_project_icon.png'))
   Label(main_frame,bg='#fff',image=icon).pack()
   hr_width=Frame(frm,width=2,height=frm.winfo_screenheight(),bg='#A9A9A9')
   hr_width.place(x=82,y=0)
   hr_height=Frame(frm,width=frm.winfo_screenwidth(),height=3,bg='#A9A9A9')
   hr_height.place(x=83,y=97)
   Mail_Messages_frame=Frame(frm,width=frm.winfo_screenwidth()-110, height=frm.winfo_screenheight()-100,bg='#fff' )
   Mail_Messages_frame.place(x=90,y=100) 
   x_Main_Mail=90
   y_Main_Mail=100
   Emails_Number,lis_Of_Emails=EmailReciverExtra.Find_Emails(mail=mail,password=password)
   
   for message in reversed(lis_Of_Emails):
       Subject=message.get('Subject')
       if Subject is None or Subject=='':
           Subject='No subject'
       From=message.get('From')
       Date_Of_Email=message.get('Date')
       content=None
       FindFile=False
       NameOfFile=None
       for part in message.walk():
            if part.get_content_type() =='text/plain':
                content=part.as_string()
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            if bool(fileName):
                FindFile=True
                filePath = os.path.join('CDRRoom', fileName)
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                NameOfFile=fileName
       x_Main_Mail=x_Main_Mail
       Button(Mail_Messages_frame,bg='#fff',text=str('subject:'+Subject),width=14,height=1,font='Arial 10 bold',border=0).place(x=x_Main_Mail,y=y_Main_Mail)
       Label(Mail_Messages_frame,bg='#fff',text=Date_Of_Email,width=16,height=2,border=0).place(x=x_Main_Mail+600,y=y_Main_Mail)
       Label(Mail_Messages_frame,bg='#fff' ,text=str('From: '+From,),font='Arial 12 bold').place(x=x_Main_Mail+40,y=y_Main_Mail+40)
       if NameOfFile is not None:
           file_to_cdr=PDFprocessor.Clean_Pdf_From_ClickAbles(filename=NameOfFile)
           Button(Mail_Messages_frame,bg='#fff' ,text='Email file',font='Arial 14 bold',command=lambda:open_file_to_read('C:\\temp\\NAC\\FinalProject\\CDRFP\\CDRFinal\\CDR_Processor\\'+file_to_cdr)).place(x=x_Main_Mail,y=y_Main_Mail+80)
    #    Frame(frm,width=frm.winfo_screenwidth(),height=3,bg='#A9A9A9').place(x=x_Main_Mail,y=y_Main_Mail+30)
       y_Main_Mail=y_Main_Mail+110
   frm.mainloop()

def open_file_to_read(full_file_path):
    os.startfile(full_file_path)


# CDR_Mail_form('cdrpro2022@gmail.com','uqsnaaeoxnigvftu',None)
loginScreen()