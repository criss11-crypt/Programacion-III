import tkinter as tk

class Applications:
    def __init__(self):
        self.valor = 1
        self.ventana01 = tk.Tk()
        self.ventana01.title("Botones")

        self.label01 = tk.Label(self.ventana01, text=self.valor, font=("Arial", 14))
        self.label01.grid(column=0, row=0, columnspan=2, pady=10)
        self.label01.configure(foreground='grey')

        # Botón Sumar
        self.boton01 = tk.Button(self.ventana01, text='Sumar', command=self.sumar, width=10)
        self.boton01.grid(column=0, row=1, padx=5, pady=5)

        # Botón Restar
        self.boton02 = tk.Button(self.ventana01, text='Restar', command=self.restar, width=10)
        self.boton02.grid(column=1, row=1, padx=5, pady=5)

        self.ventana01.mainloop()

    def sumar(self):
        self.valor += 1
        self.label01.config(text=self.valor)

    def restar(self):
        self.valor -= 1
        self.label01.config(text=self.valor)

# Instancia y ejecuta la aplicación
ejecutar = Applications()
