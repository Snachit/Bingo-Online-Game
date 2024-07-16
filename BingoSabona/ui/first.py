import tkinter as tk
import cv2
from PIL import Image, ImageTk
import subprocess
import pygame

class VideoBackgroundApp:
    def __init__(self, root, video_source=0):
        self.root = root
        self.root.title("Bingoo Sabona")
        # Initialize pygame mixer
        pygame.mixer.init()
        # Load the sound file
        
        pygame.mixer.music.load("img/first_sound.mp3")
            # Play the sound in an infinite loop (-1)
        pygame.mixer.music.play(-1)
        
        
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.canvas = tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()

        self.delay = 10
        self.update()

        self.root.bind('a', self.switch_page)

    def update(self):
        ret, frame = self.vid.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        else:
            self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.root.after(self.delay, self.update)

    def switch_page(self, event):
        self.root.destroy()
        pygame.mixer.music.stop()
        subprocess.run(["python", "sign-up.py"])

    def __del__(self):
        if hasattr(self, 'vid') and self.vid.isOpened():
            self.vid.release()

root = tk.Tk()
root.title('Bingoo Sabona')
root.geometry("1000x800")
root.resizable(False, False)
video_source = "img/Bingoo.mp4"

app = VideoBackgroundApp(root, video_source)

root.mainloop()
