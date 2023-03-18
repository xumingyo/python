# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:50:24 2023

@author: User
"""

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
#window2 = tk.Tk();

window.title("QQ")

window.geometry('300x300')

label = tk.Label(window,text="我的GUI",bg="#05A",fg="#5FC")

label.pack()

entry = tk.Entry(window,width = 20)

entry.pack()

def clickMe():
    tkinter.messagebox.showinfo(title='提示',message='好痛')

button = tk.Button(window,text = "按鈕",command=clickMe)

button.pack();

#window2.title("QQ!!")

#window2.geometry('300x300')

window.mainloop()
#window2.mainloop()



