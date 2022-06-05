from tkinter import *
from tkinter import messagebox

login_screen=Tk()
def loginScreen():
    login_screen.title('CDR-login')
    login_screen.geometry('950x520+300+200')
    login_screen.configure(bg='#fff')
    login_screen.resizable(False,False)
    Bg_img=PhotoImage(file='images/My_Login.png')
    img_label=Label(login_screen,image=Bg_img,bg='white').place(x=50,y=50)
    frame=Frame(login_screen,width=350,height=350,bg='white')

    frame.place(x=480,y=70)
    fnt=('Microsft YaHei UI Light',25)
    heading=Label(frame,text="Sign in" ,font=fnt,bg='white',fg='#57a1f8').place(x=100,y=5)

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

    Login_btn=Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0).place(x=35,y=204)
    Label(frame,text="Don't have an account?",fg='black',bg='white',font= ('Microsft YaHei UI Light',9)).place(x=75,y=270)
    sign_up_btn=Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg='#57a1f8')
    sign_up_btn.place(x=215,y=270)



    login_screen.mainloop()




register_screen=Tk()
def Register_Screen():
    register_screen.title('CDR-register')
    register_screen.geometry('950x520+300+200')
    register_screen.configure(bg='#fff')
    register_screen.resizable(False,False)

    frame=Frame(register_screen,width=350,height=350,bg='white')

    frame.place(x=480,y=70)
    fnt=('Microsft YaHei UI Light',25)
    heading=Label(frame,text="Sign up" ,font=fnt,bg='white',fg='#57a1f8').place(x=100,y=5)

    ##################################################
    def on_enter(e):
        Email.delete(0,'end')

    def on_leave(e):
        name=Email.get()
        if name=='':
            Email.insert(0,'Email')
    Email_val=StringVar()
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
    password_val=StringVar()
    password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
    password.place(x=30,y=150)
    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    password.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=174)
    ##################################################

     ##################################################
    def on_enter(e):
         app_password.delete(0,'end')

    def on_leave(e):
        name=app_password.get()
        if name =='':
            app_password.insert(0,'App Password')
    app_password_val=StringVar()
    app_password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
    app_password.place(x=30,y=150)
    app_password.insert(0,'Password')
    app_password.bind('<FocusIn>',on_enter)
    app_password.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=174)
    ##################################################

    Login_btn=Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0).place(x=35,y=204)
    Label(frame,text="Don't have an account?",fg='black',bg='white',font= ('Microsft YaHei UI Light',9)).place(x=75,y=270)
    sign_up_btn=Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg='#57a1f8')
    sign_up_btn.place(x=215,y=270)
    register_screen.mainloop()


def validation_login(username,password):
    return True
                
    


#loginScreen()
Register_Screen()