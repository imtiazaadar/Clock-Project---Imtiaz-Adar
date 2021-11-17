# Imtiaz Adar
# Email : imtiaz-adar@hotmail.com
# Phone : +8801778767775
# Project Name : Clock
# Programming Language : Python
# Date : 17/11/2021

from tkinter import *
from time import strftime

# setup
root = Tk()
root.title("CLOCK BY IMTIAZ ADAR")
width = 981
height = 702
x = 250
y = 40
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
root.resizable(0, 0)
root.iconbitmap('cl3.ico')
root.configure(background="black")

# time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# design
intro = "TIME --"
intro2 = "DATE --"
intro3 = "DAY --"
intro4 = "Made By IMTIAZ ADAR"
labelintro = Label(root, text=intro, font=("ds-digital", 80), bg="black", fg="cyan", justify="center")
labelintro.place(x=80,y=70)
label = Label(root, font=("ds-digital", 80), bg="black", fg="cyan")
label.place(x=405, y=70)
labelintro2 = Label(root, text=intro2, font=("ds-digital", 80), bg="black", fg="cyan", justify="center")
labelintro2.place(x=80,y=230)
label2 = Label(root, font=("ds-digital", 80), bg="black", fg="cyan")
label2.place(x=425, y=230)
labelintro3 = Label(root, text=intro3, font=("ds-digital", 80), bg="black", fg="cyan", justify="center")
labelintro3.place(x=80,y=390)
label3 = Label(root, font=("ds-digital", 80), bg="black", fg="cyan")
label3.place(x=382, y=390)
labelintro4 = Label(root, text=intro4, font=("ds-digital", 30), bg="black", fg="cyan", justify="center")
labelintro4.place(x=320,y=590)
string2 = strftime("%d %b %Y")
label2.config(text=string2)
string3 = strftime("%A")
label3.config(text=string3)

# driver
time()
root.mainloop()