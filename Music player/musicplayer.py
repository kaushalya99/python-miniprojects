from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#01a2b3")
root.resizable(False, False)

mixer.init()

#icon

image_icon = PhotoImage(file="C:\Users\HP\PycharmProjects\python-mini projects\Music player\assets\logo.png")
root.iconphoto(False, image_icon)

Top = PhotoImage(file="C:\Users\HP\PycharmProjects\python-mini projects\Music player\assets\top.png")
top_label = Label(root, image=Top, bg="#01a2b3")
top_label.pack()

# Keep a reference to the image objects
root.image_icon = image_icon
root.Top = Top

root.mainloop()

