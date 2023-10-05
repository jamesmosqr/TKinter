import tkinter as tk
from tkinter import ttk


vent = tk.Tk()
vent.title('Entry con manejo de variables')
vent.geometry("600x400")  # ancho x alto
vent.iconbitmap("proyecto/favicon.ico")
vent.resizable(False, False)

def guardar():
    valor = var1.get()
    print("Valor guardado en la variable:", valor)

def cerrar():
    vent.destroy()
    
var1 = tk.StringVar(value="")
txt1 = ttk.Entry(vent, width=30, textvariable=var1)
txt1.grid(row=0, column=0)

btn1 = ttk.Button(vent, text="Enviar", command=guardar)
btn1.grid(row=0, column=1)

btn2 = ttk.Button(vent, text="Cerrar Ventana", command=cerrar)
btn2.grid(row=2, column=0)


vent.mainloop()
