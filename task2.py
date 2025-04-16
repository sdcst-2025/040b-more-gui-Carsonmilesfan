import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("650x575")

ninphoto = PhotoImage(file="logo.png")
label1 = tk.Label(window, image=ninphoto)
miniphoto = PhotoImage(file="minimap.png")
label2 = tk.Label(window, image=miniphoto)
mainphoto = PhotoImage(file="main.png")
label3 = tk.Label(window, image=mainphoto)
compassphoto = PhotoImage(file="compass.png")
label4 = tk.Label(window, image=compassphoto)
button1 = tk.Button(window,text="MAP")
button2 = tk.Button(window,text="INVENTORY")
button3 = tk.Button(window,text="POKEDEX")
button4 = tk.Button(window,text="ROSTER")
button5 = tk.Button(window,text="JOURNAL")
button6 = tk.Button(window,text="HELP")
button7 = tk.Button(window,text="SHOP")
label5 = tk.Label(window,text="MINI MAP")

label1.place(x = 250,y = 500)
label2.place(x = 530,y = 75)
label3.place(x = 25,y = 25)
label4.place(x = 15,y = 470)
button1.place(x = 530,y = 175, width = 102, height = 40)
button2.place(x = 530,y = 215, width = 102, height = 40)
button3.place(x = 530,y = 255, width = 102, height = 40)
button4.place(x = 530,y = 295, width = 102, height = 40)
button5.place(x = 530,y = 335, width = 102, height = 40)
button6.place(x = 530,y = 375, width = 102, height = 40)
button7.place(x = 530,y = 415, width = 102, height = 40)
label5.place(x = 552,y = 50)

window.mainloop()