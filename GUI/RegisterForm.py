from tkinter import *
from tkinter import messagebox
import FirebaseDB
import LoginForm


def Register_Screen():
    register_screen=Tk()
    register_screen.title('CDR-sign up')
    register_screen.geometry('950x520+300+200')
    register_screen.configure(bg='#fff')
    register_screen.resizable(False,False)
    img=PhotoImage(file='images/My_Login.png')
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
    Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin_btn).place(x=180,y=335)
    register_screen.mainloop()

def signin_btn():
    
    LoginForm.loginScreen()
