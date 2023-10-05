from tkinter import *

vent= Tk()
vent.title("Ejemplo de Campos y Etiquetas")
vent.geometry("400x200")
vent.iconbitmap("proyecto/favicon.ico")

# Etiqueta 1
lbl1 = Label(vent, text="Nombre:")
lbl1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Campo de entrada 1
txt1 = Entry(vent)
txt1.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta 2
lbl2 = Label(vent, text="Apellido:")
lbl2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Campo de entrada 2
txt2 = Entry(vent)
txt2.grid(row=1, column=1, padx=10, pady=10)

vent.mainloop()
