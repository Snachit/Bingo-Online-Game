import tkinter as tk
from tkinter import Tk, Canvas, Label, Entry, Button, messagebox, Toplevel
import mysql.connector
import subprocess
from PIL import Image, ImageTk

class LoginFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingoo Bingoo')
        self.root.geometry("1000x800")
        self.root.resizable(False, False)

        self.canvas = Canvas(root, width=1000, height=800, bg='black')
        self.canvas.pack()

        self.label2 = Label(self.canvas, font=('calibri', 50, 'bold'), text='Score :', foreground='red', background='black')
        self.label2.place(x=300, y=50)

        self.label2 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Name :', foreground='white', background='black')
        self.label2.place(x=100, y=200)

        self.label3 = Label(self.canvas, font=('calibri', 20, 'bold'), text='', foreground='white', background='black')
        self.label3.place(x=100, y=250)

        self.label4 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Email :', foreground='white', background='black')
        self.label4.place(x=100, y=350)

        self.label5 = Label(self.canvas, font=('calibri', 20, 'bold'), text='', foreground='white', background='black')
        self.label5.place(x=100, y=400)

        self.label6 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Password :', foreground='white', background='black')
        self.label6.place(x=100, y=500)

        self.label7 = Label(self.canvas, font=('calibri', 20, 'bold'), text='', foreground='white', background='black')
        self.label7.place(x=100, y=550)

        self.label8 = Label(self.canvas, font=('calibri', 20, 'bold'), text='New Name :', foreground='white', background='black')
        self.label8.place(x=445, y=200)

        self.en1 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en1.place(x=400, y=250, width=240, height=40)

        self.label9 = Label(self.canvas, font=('calibri', 20, 'bold'), text='New Email :', foreground='white', background='black')
        self.label9.place(x=440, y=350)

        self.en2 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en2.place(x=400, y=400, width=240, height=40)

        self.label10 = Label(self.canvas, font=('calibri', 20, 'bold'), text='New Password :', foreground='white', background='black')
        self.label10.place(x=430, y=500)

        self.en3 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en3.place(x=400, y=550, width=240, height=40)

        self.b2 = Button(self.canvas, text='Change', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.change_name)
        self.b2.place(x=750, y=250, width=240, height=40)

        self.b3 = Button(self.canvas, text='Change', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.change_email)
        self.b3.place(x=750, y=400, width=240, height=40)

        self.b4 = Button(self.canvas, text='Change', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.change_password)
        self.b4.place(x=750, y=550, width=240, height=40)

        self.b5 = Button(self.canvas, text='Log Out', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.switch_page1)
        self.b5.place(x=240, y=700, width=240, height=40)

        self.b6 = Button(self.canvas, text='Quitter', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.Quitter)
        self.b6.place(x=520, y=700, width=240, height=40)

        self.setup_database_connection()
        self.mycursor.execute("SELECT name FROM users WHERE email = (SELECT email FROM playNow Order by id desc limit 1)")
                
        name = self.mycursor.fetchone()

        if name:
            username = name[0]
            self.label3.config(text=f"{username}")

        self.mycursor.execute("SELECT email FROM users WHERE email = (SELECT email FROM playNow Order by id desc limit 1)")
                
        email = self.mycursor.fetchone()

        if email:
            email1 = email[0]
            self.label5.config(text=f"{email1}")

        self.mycursor.execute("SELECT psd FROM users WHERE email = (SELECT email FROM playNow Order by id desc limit 1)")

        password = self.mycursor.fetchone()
        if password:
            psd = password[0]
            self.label7.config(text=f"{psd}")

    def setup_database_connection(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FUTH3494",
            database="game"
        )
        self.mycursor = self.mydb.cursor()

    def change_name(self):
        new_name = self.en1.get()
        self.mycursor.execute("UPDATE users SET name = %s WHERE email = (SELECT email FROM playNow Order by id desc limit 1)", (new_name,))
        self.mydb.commit()
        messagebox.showinfo("Success", "Name changed successfully!")
        root.destroy()
        subprocess.run(["python", "playerInterface.py"])

    def change_email(self):
        new_email = self.en2.get()
        self.mycursor.execute("UPDATE users SET email = %s WHERE email = (SELECT email FROM playNow Order by id desc limit 1)", (new_email,))
        self.mydb.commit()
        messagebox.showinfo("Success", "Email changed successfully!")
        root.destroy()
        subprocess.run(["python", "playerInterface.py"])

    def change_password(self):
        new_password = self.en3.get()
        self.mycursor.execute("UPDATE users SET password = %s WHERE email = (SELECT email FROM playNow Order by id desc limit 1)", (new_password,))
        self.mydb.commit()
        messagebox.showinfo("Success", "Password changed successfully!")
        root.destroy()
        subprocess.run(["python", "playerInterface.py"])

    def switch_page1(self):
        root.destroy()
        subprocess.run(["python", "sign-in.py"])

    def Quitter(self):
        self.root.destroy()
        self.root.quit()


root = Tk()

app = LoginFormApp(root)

root.mainloop()
