from tkinter import *
from tkinter import colorchooser
import tkinter as tk

color_main = tk. Tk()
color_main.title = ('demo color picker')
color_main.iconbitmap = ('D:\color_picker')
color_main.geometry = ('600x400+50+50')

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(color_main, text=my_color).pack()
    my_label2 = Label(color_main, text="the color that you pick", font=("sans-serif", 32, "bold"), bg=my_color).pack(pady=5)

my_button = Button(color_main, text="pick the color", command=color).pack(pady=50)

color_main.mainloop()