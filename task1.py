import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("375x150")

label1 = tk.Label(window, text = 'Principal')
label2 = tk.Label(window, text = 'Interest Rate')
label3 = tk.Label(window, text = 'Years')
label4 = tk.Label(window, text = 'Amount')
label5 = tk.Label(window, text = '-')
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)

label1.place(x =50 ,y =25 )
label2.place(x =150 ,y =25 )
label3.place(x =300 ,y =25 )
label4.place(x =75 ,y =125 )
entry1.place(x =0 ,y =50 )
entry2.place(x =125 ,y =50 )
entry3.place(x =125 ,y =125 )
label5.place(x =50 ,y =75 )
entry4.place(x =250 ,y =50 )



window.mainloop()