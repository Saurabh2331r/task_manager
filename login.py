from customtkinter import *
from tkinter import messagebox
from PIL import Image
import database

#function

def login():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("Error","All fields are required")

    elif database.login_check(usernameEntry.get(),passwordEntry.get()):

        messagebox.showinfo("Success","Login is Successful")
        database.create_database(usernameEntry.get())
        root.destroy()
        import task_manager
    else:
        messagebox.showerror("Error","Invalid Credentials")
        usernameEntry.delete(0,END)
        passwordEntry.delete(0,END)


#GUI
root=CTk()

root.geometry("1000x420+50+50")
root.resizable(0,0)

root.configure(fg_color="#fff")


root.title("Login Page")


logo=CTkImage(Image.open('login.png'),size=(480,400))
logoLabel=CTkLabel(root,image=logo,text="")
logoLabel.place(x=0,y=0)


heading=CTkLabel(root,text="Task Manager Login",font=("Gordy Old Style",25,"bold"),text_color="#000")
heading.place(x=650,y=100)

usernameEntry=CTkEntry(root,placeholder_text="Enter Your Username",width=180,fg_color="#fff",text_color="#000")
usernameEntry.place(x=680,y=150)

passwordEntry=CTkEntry(root,placeholder_text="Enter Your Password",width=180,show="*",fg_color="#fff",text_color="#000")
passwordEntry.place(x=680,y=200)

loginButton=CTkButton(root,text="Login",cursor="hand2",command=login)
loginButton.place(x=700,y=250)



root.mainloop()