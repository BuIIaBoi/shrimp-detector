from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

def detection():
    answer = messagebox.askyesno("Message", "Are you a shrimp?")
    if(answer == True):
        window.destroy()
        whale()
    else:
        window.destroy()
        messagebox.showinfo("Message", "You are not a shrimp.")



def whale():
    new_window = Tk()
    new_window.geometry("1920x1080")
    new_window.title(" ")

    whale_icon = PhotoImage(file="Other\\whale.png")
    new_window.iconphoto(True, whale_icon)

    pygame.mixer.init()

    whale = Image.open("Other\\whale.png")
    whale = whale.resize((1920, 1080))
    whale = ImageTk.PhotoImage(whale)

    new_label = Label(new_window, image=whale, compound="bottom")
    new_label.image = whale

    pygame.mixer.music.load("Other\\cat_laughing.mp3")
    pygame.mixer.music.play(loops=-1)

    new_label.pack()    
    new_window.mainloop()

window = Tk()
window.geometry("500x500")
window.config(background="white")

icon = PhotoImage(file="Other\\shrimp.png")
window.iconphoto(True, icon)
window.title("Shrimp Detector")

shrimp = Image.open("Other\\shrimp.png")
shrimp = shrimp.resize((200, 200))
shrimp = ImageTk.PhotoImage(shrimp)

label = Label(window, text="Are you a shrimp?",
                font=('arial', 30, 'bold'), 
                fg='black', 
                background="white",
                bd=10,
                padx=50,
                pady=50,
                image=shrimp, compound="bottom")
label.image = shrimp

button = Button(window, text="Start Detection", command=detection, width=20, height=2, font=('arial', 20, 'bold'))

label.pack()
button.pack()

window.mainloop()