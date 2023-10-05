#grid manager
#trabajando con grid
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Manejo de grid')  # Título de la ventana
ventana.geometry("600x400")
ventana.iconbitmap("proyecto/favicon.ico")

#configurando grid
ventana.rowconfigure(0, weight=2)
ventana.columnconfigure(1,weight=10)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=5)



#metodos de los eventos
def evento1():
    btn1.config(text="Boton 1 presionado")

def evento2():
    btn2.config(text='Boton 2 presionado')

def  evento3():
    btn3.config(text='Boton 3 presionado')

def evento4():
    btn4.config(text='Boton 4 presionado', foreground="pink", relief=tk.GROOVE, background="gray")

#Creando botones
btn1 = ttk.Button(ventana, text = "Botón one", command=evento1)
btn1.grid(row=0, column=0, sticky="NSWE")

#usando sticky
#N(arriba), E(derecha), S(abajo), W(izquierda) 
btn2 = ttk.Button(ventana, text = "Boton two", command=evento2)
btn2.grid(row=1, column=0, sticky="NSWE")

btn3 = ttk.Button(ventana, text = "Botón three", command=evento3)
btn3.grid(row=0, column=1,sticky="NSWE")

btn4 = tk.Button(ventana, text = "Botón four", command=evento4)
btn4.grid(row=1, column=1,sticky="NSWE")

ventana.mainloop()
