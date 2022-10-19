#importar bibliotecas
from atexit import register
from sqlite3 import TimeFromTicks
from tkinter import *
from tkinter  import messagebox
from turtle import right
from tkinter import ttk
import Database

#criar  nossa janela

jan = Tk()
jan.title("Dp  System -  Acess panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable( width=False, height=False)
jan.attributes("-alpha",0.9)
jan.iconbitmap(default="icons/logoIcon.ico")

#carregando imagens
logo = PhotoImage(file="icons/logo.png")


LeftFrame = Frame (jan, width=200, heigh=300, bg="MIDNIGHTBLUE",relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame (jan, width=395, heigh=300, bg="MIDNIGHTBLUE",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

Userlabel = Label(RightFrame, text="Username", font=("century gothic",20), bg="MIDNIGHTBLUE", fg="white")
Userlabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150,y=110)

#

Passlabel = Label(RightFrame, text="Password", font=("century gothic",20), bg="MIDNIGHTBLUE", fg="white")
Passlabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150,y=160)


def Login():
    User =  UserEntry.get()
    Pass = PassEntry.get()
    Database.cursor.execute(""" SELECT * FROM Users
    WHERE (User = ? and Password = ?)    
    """, (User , Pass))
    print ("Selecionou")

    VerifyLogin = Database.cursor.fetchone()
    try:
            if (User in  VerifyLogin and  Pass  in VerifyLogin):
                messagebox.showinfo(title="Login info", message="Acesso confirmado. Bem vindo!")
    
    except:    
        messagebox.showinfo(title="Login info", message="Acesso negado. verifique  se  esta cadastrado no sistema!")

#Botoes



LoginButton = ttk.Button (RightFrame,text= "Login",width=30, command=Login)
LoginButton.place(x=100,y=225)


def Register():
    #removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #inserindo Widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry (RightFrame, width=38)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55) 

    EmailEntry = ttk.Entry(RightFrame, width=38)
    EmailEntry.place(x=100, y=66)  


    def RegistertoDatabase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" and  Email == "" and  User == "" and Pass == ""):
            messagebox.showerror(title="Register erro", message="Não deixe Nenhum campo vazio.Preencha Todos os campos")
        else:
            Database.cursor.execute("""
                INSERT INTO  Users (Name, Email , User,Password) VALUES(?,?,?,?)
            """,(Name,Email,User,Pass))
            Database.conn.commit()
            messagebox.showinfo(title="Regiter Info", message="Conta criada com sucesso")

    Register =ttk.Button(RightFrame, text="Register",width=30, command=RegistertoDatabase)
    Register.place(x=100,y=225)



    def BackToLogin():
    # removendo widget de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place (x=5000)
    #Trazendo de volta botao de login
    LoginButton.place(x=100)
    RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back",width=20, command=BackToLogin)
    Back.place(x=125,y=260)



RegisterButton = ttk.Button (RightFrame,text= "Register",width=20, command=Register)
RegisterButton.place(x=100,y=260)


jan.mainloop()
