# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ventana = tk.Tk()
ventana.title("Controles Tk")
ventana.config(bg="#E4E2E2")
ventana.geometry("700x400")


style = ttk.Style(ventana)
style.theme_use("clam")

style.configure("label.TLabel", background="#E4E2E2", foreground="#000")
label = ttk.Label(master=ventana, text="", style="label.TLabel")
label.place(x=237, y=34, width=80, height=40)

style.configure("button.TButton", background="#E4E2E2", foreground="#000")
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=ventana, text="Aumnetar", style="button.TButton")
button.place(x=250, y=104, width=80, height=40)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=ventana, text="Disminuir", style="button1.TButton")
button1.place(x=250, y=177, width=80, height=40)

style.configure("button2.TButton", background="#E4E2E2", foreground="#000")
style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button2 = ttk.Button(master=ventana, text="salir", style="button2.TButton")
button2.place(x=272, y=305, width=80, height=40)


ventana.mainloop()