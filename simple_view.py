print("Hello MVC")

import tkinter as tk
from tkinter import *
import time


# define the click event of the toggle
def toggle_button_click():
    global is_on
    # Determine is on or off
    if is_on:
        on_button.config(image = off)
        is_on = False
    else:
        on_button.config(image = on)
        is_on = True
    print("Button is clicked!!!")

window = tk.Tk()

window.attributes('-fullscreen', True)
window.title("Rapido Project")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)



labelAMONIACaption = tk.Label(text = "AMONIA",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 100 bold")

labelAMONIACaption.place(x=0,y=0, width = screen_width/3, height = 300)


labelTDSCaption = tk.Label(text = "TDS",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 100 bold")

labelTDSCaption.place(x=screen_width/3,y=0, width = screen_width/3, height = 300)


labelPHCaption = tk.Label(text = "PH",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 100 bold")

labelPHCaption.place(x=2*screen_width/3,y=0, width = screen_width/3, height = 300)



labelAMONIAUnit = tk.Label(text = "(PPM)",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 30 bold")

labelAMONIAUnit.place(x=0,y=280, width = screen_width/3, height = 100)


labelTDSUnit = tk.Label(text = "(NTU)",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 30 bold")

labelTDSUnit.place(x=screen_width/3,y=280, width = screen_width/3, height = 100)


labelPHUnit = tk.Label(text = "( )",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 30 bold")

labelPHUnit.place(x=2*screen_width/3,y=280, width = screen_width/3, height = 100)



labelAMONIAValue = tk.Label(text = "5.12",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 120 bold")

labelAMONIAValue.place(x=0,y=350, width = screen_width/3, height = 200)


labelTDSValue = tk.Label(text = "20",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 120 bold")

labelTDSValue.place(x=screen_width/3,y=350, width = screen_width/3, height = 200)


labelPHValue = tk.Label(text = "7.11",
                    fg = "#0000ff",
                    justify= CENTER,
                    #bg = "#000",
                    font = "Helvetica 120 bold")

labelPHValue.place(x=2*screen_width/3,y=350, width = screen_width/3, height = 200)

is_on = True
# define on and off stage of the toggle
on = PhotoImage(file = "on_button.png")
off = PhotoImage(file = "off_button.png")

on_button = Button(window, image = on, bd = 0, command = toggle_button_click, justify = CENTER)
on_button.place(x = 0 ,y = 600 ,width = screen_width)

counter = 0
cycle = 0

while True:
    cycle += 1
    if cycle >= 20:
        #print("Client is running...", counter)
        counter += 1
        cycle = 0
        labelAMONIAValue.config(text = str(counter))
        labelTDSValue.config(text = str(counter))
        labelPHValue.config(text = str(counter))
    window.update()
    time.sleep(0.1)

