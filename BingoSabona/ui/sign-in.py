import subprocess
from tkinter import Tk, Canvas, Label, Entry, Button, messagebox, Toplevel
import mysql.connector
from PIL import Image, ImageTk

class LoginFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingoo Bingoo')
        self.root.geometry("1000x800")
        self.root.resizable(False, False)

        self.background_image = Image.open("img/bgSignIn.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = Canvas(root, width=1000, height=800)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor='nw', image=self.background_photo)

        self.label1 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Email :', foreground='white', background='black')
        self.label1.place(x=380, y=170)

        self.en1 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en1.place(x=380, y=220, width=240, height=40)

        self.label2 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Password :', foreground='white', background='black')
        self.label2.place(x=380, y=270)

        self.en2 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en2.place(x=380, y=320, width=240, height=40)

        self.b1 = Button(self.canvas, text='Start', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.submit_form)
        self.b1.place(x=380, y=390, width=240, height=40)

        self.b2 = Button(self.canvas, text='Sign up', font=('calibri', 20, 'bold'), fg="white", bd=1, bg="black", relief='solid', cursor='hand2', command=self.switch_page)
        self.b2.place(x=750, y=5, width=240, height=40)

        self.label4 = Label(self.canvas, font=('calibri', 15, 'bold'), text=' u dont have an account !', foreground='red', background='black')
        self.label4.place(x=510, y=10)

    def submit_form(self):
        email = self.en1.get()
        psd = self.en2.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FUTH3494",
            database="game"
        )
        mycursor = mydb.cursor()

        query = "SELECT * FROM users WHERE email = %s AND psd = %s"
        mycursor.execute(query, (email, psd))
        user = mycursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            sql = "INSERT INTO playNow (email) VALUES (%s)"
            val = (email,)
            mycursor.execute(sql, val)
            mydb.commit()
            root.destroy()
            subprocess.run(["python", "playerInterface.py"])

            # Hide or destroy the current window
            # self.root.withdraw()  # Hide the current window

            # You can also destroy the current window if you don't need it anymore
            # root.destroy()

        else:
            messagebox.showerror("Error", "Invalid email or password!")

        self.en2.delete(0, 'end')

    def switch_page(self):
        root.destroy()
        subprocess.run(["python", "sign-up.py"])

root = Tk()

app = LoginFormApp(root)

root.mainloop()
