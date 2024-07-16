import subprocess
from tkinter import Tk, Canvas, Label, Entry, Button
from PIL import Image, ImageTk
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
from PIL import Image, ImageTk

class LoginFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingoo Bingoo')
        self.root.geometry("1000x800")
        self.root.resizable(False, False)

        self.background_image = Image.open("img/bgVer.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = Canvas(root, width=1000, height=800)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor='nw', image=self.background_photo)

        self.label1 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Verification Code :', foreground='white', background='black')
        self.label1.place(x=380, y=320)

        self.en1 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en1.place(x=380, y=375, width=240, height=40)

        self.b1 = Button(self.canvas, text='Verify', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief=SOLID, cursor='hand2', command=self.verification)
        self.b1.place(x=380, y=450, width=240, height=40)

    def verification(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FUTH3494",
            database="game"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT code FROM verCode ORDER BY id_Ver DESC LIMIT 1")

        correct_code = mycursor.fetchone()
        code = self.en1.get()
        if code == correct_code[0] :
            root.destroy()
            subprocess.run(["python", "sign-in.py"])
        else :
             messagebox.showinfo("Error", "Not correct code!")
            


root = Tk()

app = LoginFormApp(root)

root.mainloop()
