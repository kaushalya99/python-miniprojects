from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob

root=Tk()
root.title("Google translator")
root.geometry("500x500")


#icon
image_icon=PhotoImage(file="google.png")
root.iconphoto(False,image_icon)


langiage=googletrans.LANGUAGES
languageV=list(language.values())

