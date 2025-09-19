import tkinter as tk
from datetime import date
from tkinter import messagebox

def calcular_edad():
    try:
        anio = int(entry_anio.get())
        mes = int(entry_mes.get())
        dia = int(entry_dia.get())

        nacimiento = date(anio, mes, dia)  # valida automáticamente la fecha
        hoy = date.today()
        edad = hoy.year - nacimiento.year

        # Verificar si ya cumplió años este año
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        messagebox.showinfo("Resultado", f"Tienes {edad} años.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una fecha válida.")

def limpiar():
    entry_anio.delete(0, tk.END)
    entry_mes.delete(0, tk.END)
    entry_dia.delete(0, tk.END)

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("300x200")

# Etiquetas y entradas
tk.Label(ventana, text="Año de nacimiento:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
entry_anio = tk.Entry(ventana)
entry_anio.grid(row=0, column=1, pady=5)

tk.Label(ventana, text="Mes de nacimiento:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
entry_mes = tk.Entry(ventana)
entry_mes.grid(row=1, column=1, pady=5)

tk.Label(ventana, text="Día de nacimiento:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
entry_dia = tk.Entry(ventana)
entry_dia.grid(row=2, column=1, pady=5)

# Botones
btn_calcular = tk.Button(ventana, text="Calcular Edad", command=calcular_edad)
btn_calcular.grid(row=3, column=0, pady=10, padx=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.grid(row=3, column=1, pady=10, padx=5)

ventana.mainloop()