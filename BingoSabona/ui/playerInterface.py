import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
from PIL import Image, ImageTk
import cv2

class VideoBackgroundApp:
    def __init__(self, root, video_source=0):
        self.root = root
        self.root.title("Bingoo Sabona")
        
        # Initialize pygame mixer
        # pygame.mixer.init()
        # Load the sound file
        # pygame.mixer.music.load("img/first_sound.mp3")
        # Play the sound in an infinite loop (-1)
        # pygame.mixer.music.play(-1)
        
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.delay = 10
        self.update()

        self.label1 = tk.Label(self.canvas, font=('calibri', 25, 'bold'), text='', foreground='white', background='black')
        self.label1.place(x=780, y=30)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="FUTH3494",
            database="game"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT name FROM users WHERE email = (SELECT email FROM playNow Order by id desc limit 1)")
                
        last_row = mycursor.fetchone()

        if last_row:
            username = last_row[0]
            self.label1.config(text=f"Hi {username}")
        else:
            messagebox.showerror("Error", "Invalid email or password")

        mydb.close()

        self.b2 = tk.Button(self.canvas, text='⚙️', font=('calibri', 25, 'bold'), fg="gray", bd=1, bg="black", relief='solid', cursor='hand2', command=self.switch_page2)
        self.b2.place(x=940, y=20, width=50, height=68)


    def switch_page2(self):
        root.destroy()
        subprocess.run(["python", "parametre.py"])

    def update(self):
        ret, frame = self.vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 100, image=self.photo, anchor=tk.NW)
        else:
            self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.root.after(self.delay, self.update)

class LoginFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingoo Bingoo')
        self.root.geometry("1000x800")
        self.root.resizable(False, False)

        self.background_image = Image.open("img/bgInte.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.Char = Image.open("img/char.png")
        self.Char = ImageTk.PhotoImage(self.Char)

        self.canvas = tk.Canvas(root, width=1000, height=800)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor='nw', image=self.background_photo)

        # self.canvas.create_image(380, 410, anchor='nw', image=self.Char)

        self.b1 = tk.Button(self.canvas, text='Start', font=('calibri', 25, 'bold'), fg="blue", bd=1, bg="black", relief='solid', cursor='hand2', command=self.switch_page1)
        self.b1.place(x=250, y=75, width=500, height=68)


    def switch_page1(self):
        root.destroy()
        subprocess.run(["python", "testi.py"])


root = tk.Tk()
video_source = "img/playerInterface.mp4"

app = VideoBackgroundApp(root, video_source)
appl = LoginFormApp(root)

root.mainloop()
