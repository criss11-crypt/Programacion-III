import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.formulario01 = tk.Tk()
        self.formulario01.title('Operaciones')

        self.label01 = tk.Label(self.formulario01, text='Ingrese el número:')
        self.label01.grid(column=0, row=0)

        self.dato01 = tk.StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable=self.dato01)
        self.entry01.grid(column=0, row=1)

        self.boton01 = tk.Button(self.formulario01, text='Calcular', command=self.calcular)
        self.boton01.grid(column=0, row=2)

        self.label02 = tk.Label(self.formulario01, text='Resultado:')
        self.label02.grid(column=0, row=3)

        self.formulario01.mainloop()

    def calcular(self):
        try:
            valor = int(self.dato01.get())
            cuadrado = valor * valor
            self.label02.configure(text=f'Resultado: {cuadrado}')
        except ValueError:
            self.label02.configure(text="Por favor ingrese un número válido")

ejecuta = Aplicacion()
