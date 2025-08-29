import tkinter as tk

class Applications:
    def __init__(self):  # ✅ Constructor correcto con doble guion bajo
        self.valor = 1
        self.ventana01 = tk.Tk()
        self.ventana01.title("Botones")

        self.label01 = tk.Label(self.ventana01, text=self.valor)
        self.label01.grid(column=0, row=0)
        self.label01.configure(foreground='grey')

        self.boton01 = tk.Button(self.ventana01, text='Sumar', command=self.sumar)
        self.boton01.grid(column=0, row=1)

        self.ventana01.mainloop()

    def sumar(self):
        self.valor = self.valor + 1
        self.label01.config(text=self.valor)

# Instancia y ejecuta la aplicación
ejecutar = Applications()
