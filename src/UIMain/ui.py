from tkinter import *
import tkinter as tk
from tkinter import ttk

#Ventana principal
root = Tk()
root.title("POOBakery")
root.geometry("1500x1000")
#root.configure(background = "gray")

label = Label(root,text="POOBakery")
label.pack()
borde = Frame()
frame = Frame(root, bd = 1, relief=FLAT, padx = 1, pady = 1)
frame.pack(padx = 5, pady = 5, fill = "both", expand=True)
tk.Grid.rowconfigure(frame,0, weight=1)
tk.Grid.rowconfigure(frame,1, weight=2)
tk.Grid.columnconfigure(frame,0, weight=1)
tk.Grid.columnconfigure(frame,1, weight=1)

#framep1 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 0)
#framep2 = Frame(frame, bd = 5, relief=FLAT, padx = 2, pady = 2, bg = "white").grid(row =0 , column = 1)
frame1 = Frame(frame, bg = "blue").grid(row =0 , column = 0, padx = 5, pady=5, sticky="nsew")
frame2 = Frame(frame, bg = "red").grid(row =0 , column = 1, padx = 5, pady=5, sticky="nsew")
frame3 = Frame(frame, bg = "red").grid(row =1 , column = 0, padx = 5, pady=5, sticky="nsew")
frame4 = Frame(frame, bg = "blue").grid(row =1 , column = 1, padx = 5, pady=5, sticky="nsew")

imagen = PhotoImage("bienvenida.png")
bienvenida = Label(frame1, image=imagen)


root.mainloop()