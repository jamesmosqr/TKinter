#probando elementos dentro de la interfaz
import tkinter as tk

from tkinter import ttk
#se usa para los componentes de tkinter

# Se crea el objeto ventana para crear la interfaz
ventana = tk.Tk()

# Se asigna la dimensión que va a tomar la pantalla
ventana.geometry('600x400')

# Se agrega un título al programa
ventana.title("Registro usuario")

def eventClic():
    btn1.config(text="Ejecutando....") #hace las veces de mouseHover
    print("SE ha ejecutado el botón")

# def eventClics():
#     btn2.config(text="Ejecutando....") #hace las veces de mouseHover
#     print("Se ha ejecutado el otro botón")

btn1 = ttk.Button(ventana, text="clic aqui", command=eventClic)
btn1.pack()
#Se ejecuta la aplicación y se hace visible el boton

btn2 = tk.Button(ventana, text="Nuevo botón ")
btn2.pack()

# Se entrega el componente mainloop() para indicar que la ventana sea visible
ventana.mainloop()
