#trabajando con grid
import tkinter as tk # GUI
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Manejo de grid')  # Título de la ventana
ventana.geometry("600x400")
ventana.iconbitmap("proyecto/favicon.ico")


#metodos de los eventos
def evento1():
    btn1.config(text="Boton 1 presionado")

def evento2():
    btn2.config(text='Boton 2 presionado')

#Creando botones
btn1 = ttk.Button(ventana, text = "Botón one", command=evento1)
btn1.grid(row=0, column=0)




btn2 = ttk.Button(ventana, text = "Boton two", command=evento2)
btn2.grid(row=1, column=0)


ventana.mainloop()
