import customtkinter as ctk
import speech_recognition as sr
from tkinter import messagebox, Listbox, filedialog
import requests
from PIL import Image
import webbrowser
import os

def seda():
    result = sr.Recognizer()
    with sr.Microphone() as source:
        audio = result.listen(source, timeout=None, phrase_time_limit=50)
        text=result.recognize_google(audio, language='Fa-IR')
        name_list.insert(0,text)
        if "گوگل" in text:
            serch=text.replace("گوگل","").strip()
            if serch :
                webbrowser.open(serch)



root = ctk.CTk()
root.geometry("800x400")
root.resizable(False, False)

ctk.CTkLabel(root, text="سخن بگو ای مرد", font=("Arial", 20, "bold"), bg_color="purple").grid(column=1, row=0)
but_rec = ctk.CTkButton(root, text="REC", fg_color="white", font=("Arial", 20, "bold"), command=seda)
but_rec.grid(column=1, row=1)
ctk.CTkLabel(root, text="حرف های مرد زیبا", font=("Arial", 20, "bold")).grid(column=1, row=2)
name_list = Listbox(root, bg="white", font=("Arial", 20), width=30, height=7, justify="right")
name_list.grid(column=1, row=3)
but_ax = ctk.CTkButton(root, text="upload", fg_color="white", font=("Arial", 20, "bold"), command=ax)
but_ax.grid(column=1, row=4)


blinking = True
def blink():
    if blinking:
        asli_color = but_rec.cget("fg_color")
        new_color = "red" if asli_color == "gray20" else "gray20"
        but_rec.configure(fg_color=new_color)
        root.after(500, blink)

blink()
root.mainloop()
