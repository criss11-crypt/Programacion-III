import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ventana = tk.Tk()
ventana.title("Controles Tk")
ventana.config(bg="#E4E2E2")
ventana.geometry("700x400")

# Estilos
style = ttk.Style(ventana)
style.theme_use("clam")

# Variable para el valor del contador
valor = tk.IntVar(value=0)

# Label contador
style.configure("label.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 16, "bold"))
label = ttk.Label(master=ventana, textvariable=valor, style="label.TLabel", anchor="center")
label.place(x=280, y=40, width=120, height=40)

# Funciones de contador
def aumenta():
    valor.set(valor.get() + 1)

def disminuir():
    valor.set(valor.get() - 1)

def salir():
    ventana.destroy()

# --- Función para aplicar el color seleccionado ---
def cambiar_color():
    color = radio_var.get()
    if color == 1:
        ventana.config(bg="red")
        style.configure("label.TLabel", background="red", foreground="white")
    elif color == 2:
        ventana.config(bg="blue")
        style.configure("label.TLabel", background="blue", foreground="white")
    elif color == 3:
        ventana.config(bg="green")
        style.configure("label.TLabel", background="green", foreground="black")
    elif color == 4:
        ventana.config(bg="salmon")
        style.configure("label.TLabel", background="salmon", foreground="black")

# Botones con estilo
style.configure("boton.TButton", font=("Arial", 12, "bold"), padding=6)

button = ttk.Button(master=ventana, text="Aumentar", style="boton.TButton", command=aumenta)
button.place(x=100, y=120, width=120, height=40)

button1 = ttk.Button(master=ventana, text="Disminuir", style="boton.TButton", command=disminuir)
button1.place(x=100, y=180, width=120, height=40)

button2 = ttk.Button(master=ventana, text="Salir", style="boton.TButton", command=salir)
button2.place(x=100, y=240, width=120, height=40)

# --- Radiobuttons ---
radio_var = tk.IntVar(value=0)

style.configure("radio.TRadiobutton", font=("Arial", 11))

radio_rojo = ttk.Radiobutton(master=ventana, variable=radio_var, text="Rojo", value=1, style="radio.TRadiobutton")
radio_rojo.place(x=300, y=120)

radio_azul = ttk.Radiobutton(master=ventana, variable=radio_var, text="Azul", value=2, style="radio.TRadiobutton")
radio_azul.place(x=300, y=160)

radio_verde = ttk.Radiobutton(master=ventana, variable=radio_var, text="Verde", value=3, style="radio.TRadiobutton")
radio_verde.place(x=300, y=200)

radio_salmon = ttk.Radiobutton(master=ventana, variable=radio_var, text="Salmon", value=4, style="radio.TRadiobutton")
radio_salmon.place(x=300, y=240)

# --- Botón Cambiar ---
button_color = ttk.Button(master=ventana, text="Cambiar", style="boton.TButton", command=cambiar_color)
button_color.place(x=300, y=280, width=120, height=40)

ventana.mainloop()
