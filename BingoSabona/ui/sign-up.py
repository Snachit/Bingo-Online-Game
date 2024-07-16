from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
from PIL import Image, ImageTk
import re
from email.message import EmailMessage
import ssl
import smtplib
import random
import string

class RegistrationFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingoo Bingoo')
        self.root.geometry("1000x800")
        self.root.resizable(False, False)

        self.background_image = Image.open("img/bgSignUp.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = Canvas(root, width=1000, height=800)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        self.label1 = Label(self.canvas, font=('calibri', 20, 'bold'), text='UserName :', background='black', foreground='white')
        self.label1.place(x=380, y=70)

        self.en1 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en1.place(x=380, y=120, width=240, height=40)

        self.label2 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Email :', background='black', foreground='white')
        self.label2.place(x=380, y=170)

        self.en2 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en2.place(x=380, y=220, width=240, height=40)

        self.label3 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Password :', background='black', foreground='white')
        self.label3.place(x=380, y=270)

        self.en3 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en3.place(x=380, y=320, width=240, height=40)

        self.label4 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Confirm Password :', background='black', foreground='white')
        self.label4.place(x=380, y=370)

        self.en4 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en4.place(x=380, y=420, width=240, height=40)

        self.b1 = Button(self.canvas, text='Submit', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief=SOLID, cursor='hand2', command=self.submit_form)
        self.b1.place(x=380, y=490, width=240, height=40)

        self.b2 = Button(self.canvas, text='Sign in', font=('calibri', 20, 'bold'), fg="white", bd=1, bg="black", relief=SOLID, cursor='hand2', command=self.switch_page)
        self.b2.place(x=750, y=5, width=240, height=40)

        self.label5 = Label(self.canvas, font=('calibri', 15, 'bold'), text='Already have an account!', background='black', foreground='red')
        self.label5.place(x=505, y=10)

    def submit_form(self):

        username = self.en1.get()
        email = self.en2.get()
        psd = self.en3.get()
        confirm_psd = self.en4.get()

        if len(username) > 7:
            messagebox.showerror("Error", "The name must be 7 characters or less!")
            return

        if psd != confirm_psd:
            messagebox.showerror("Error", "Password Error!")
            return
        
        if not re.match(r"[A-Za-z0-9.]+@gmail\.com", email):
            messagebox.showerror("Error", "Invalid email format!")
            return


        if len(psd) < 8:
            messagebox.showerror("Error", "Password should be at least 8 characters long!")
            return


        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FUTH3494",
            database="game"
        )
        mycursor = mydb.cursor()


        mycursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = mycursor.fetchone()
        if existing_user:
            messagebox.showerror("Error", "Email already exists!")
            return

        sql = "INSERT INTO users (name, email, psd) VALUES (%s, %s, %s)"
        val = (username, email, psd)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Data submitted successfully!")

        self.en1.delete(0, 'end')  
        self.en2.delete(0, 'end')  
        self.en3.delete(0, 'end')  
        self.en4.delete(0, 'end') 
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        email_s = 'bingoobingoogame@gmail.com '
        email_psd = 'lufl vjcn yjah qbyp' 

        sub = 'Welcome to BingooSabona Game'
        boody = """
Hi,

Your code is: {}. Use it to access your account.

If you didn't request this, simply ignore this message.

Yours,
The BingooSabona Team
        """.format(code)

        em = EmailMessage()
        em['From'] = email_s
        em['To'] = email  # Join multiple recipients with commas
        em['Subject'] = sub
        em.set_content(boody)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_s, email_psd)
            smtp.send_message(em)

        sql = "INSERT INTO verCode ( email, code) VALUES (%s, %s)"
        val = (email, code)
        mycursor.execute(sql, val)
        mydb.commit()
        root.destroy()
        subprocess.run(["python", "verfication_email.py"])

        

    def switch_page(self):
        root.destroy()
        subprocess.run(["python", "sign-in.py"])



root = Tk()


app = RegistrationFormApp(root)

root.mainloop()
