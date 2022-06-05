from tkinter import *
from tkinter import messagebox
import FirebaseDB

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
    Label(frame,text="Don't have an account?",fg='black',bg='white',font= ('Microsft YaHei UI Light',9)).place(x=35,y=270)
    sign_up_btn=Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg='#57a1f8').place(x=90,y=340)
    sign_up_btn.place(x=90,y=340)



    login_screen.mainloop()






def validation_login(email,password):
    user_info=FirebaseDB.database.child('Users').child(str(email.split('@')[0])).get()
    if user_info is None:
        messagebox.showerror('Invaild' ,'Wrong Email or password!')
    else:
        if user_info['password'] is not None :
            if user_info['password']==password:
                enter_method()
            else:
                messagebox.showerror('Invaild','incorrect password!')
                
def enter_method():
    print('ok')
    return True