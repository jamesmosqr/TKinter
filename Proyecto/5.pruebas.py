# import tkinter as tk

# def saludar():
#     print("Hola, mundo!")

# # Creamos la ventana
# ventana = tk.Tk()

# # Creamos el botón
# boton = tk.Button(ventana, text="Hola, mundo!", command=saludar)

# # Agregamos el botón a la ventana
# boton.pack()

# # Mostramos la ventana
# ventana.mainloop()

# import tkinter as tk

# # Creamos la ventana
# ventana = tk.Tk()

# # Cargamos la imagen del icono
# icon = tk.PhotoImage(file="favicon.ico")

# # Configuramos el icono de la ventana
# ventana.iconphoto(icon)

# # Mostramos la ventana
# ventana.mainloop()

# import tkinter module
# from tkinter import * 
# from tkinter.ttk import *

# master = Tk()

# master.geometry("600x400")
# master.title("Este es el titulo")

# # creating main tkinter window/toplevel

# # this will create a label widget
# l1 = Label(master, text = "First:")
# l2 = Label(master, text = "Second:")

# # grid method to arrange labels in respective
# # rows and columns as specified
# l1.grid(row = 0, column = 0, sticky = W, pady = 2)
# l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# # entry widgets, used to take entry from user
# e1 = Entry(master)
# e2 = Entry(master)

# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)

# # infinite loop which can be terminated by keyboard
# # or mouse interrupt
# mainloop()



# # Imports tkinter and ttk module
# from tkinter import *
# from tkinter.ttk import *

# # toplevel window
# root = Tk()

# # method to make widget invisible
# # or remove from toplevel
# def forget(widget):

# 	# This will remove the widget from toplevel
# 	# basically widget do not get deleted
# 	# it just becomes invisible and loses its position
# 	# and can be retrieve
# 	widget.forget()

# # method to make widget visible
# def retrieve(widget):
# 	widget.pack(fill = BOTH, expand = True)

# # Button widgets
# b1 = Button(root, text = "Btn 1")
# b1.pack(fill = BOTH, expand = True)

# # See, in command forget() method is passed
# b2 = Button(root, text = "Btn 2", command = lambda : forget(b1))
# b2.pack(fill = BOTH, expand = True)

# # In command retrieve() method is passed
# b3 = Button(root, text = "Btn 3", command = lambda : retrieve(b1))
# b3.pack(fill = BOTH, expand = True)

# # infinite loop, interrupted by keyboard or mouse
# mainloop()


# # Imports tkinter and ttk module
# from tkinter import *
# from tkinter.ttk import *

# # toplevel window
# root = Tk()

# # method to make widget invisible
# # or remove from toplevel
# def forget(widget):

# 	# This will remove the widget from toplevel
# 	# basically widget do not get deleted
# 	# it just becomes invisible and loses its position
# 	# and can be retrieve
# 	widget.grid_forget()

# # method to make widget visible
# def retrieve(widget):
# 	widget.grid(row = 0, column = 0, ipady = 10, pady = 10, padx = 5)

# # Button widgets
# b1 = Button(root, text = "Btn 1")
# b1.grid(row = 0, column = 0, ipady = 10, pady = 10, padx = 5)

# # See, in command forget() method is passed
# b2 = Button(root, text = "Btn 2", command = lambda : forget(b1))
# b2.grid(row = 0, column = 1, ipady = 10, pady = 10, padx = 5)

# # In command retrieve() method is passed
# b3 = Button(root, text = "Btn 3", command = lambda : retrieve(b1))
# b3.grid(row = 0, column = 2, ipady = 10, pady = 10, padx = 5)

# # infinite loop, interrupted by keyboard or mouse
# mainloop()

# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

#https://www.pythontutorial.net/tkinter/tkinter-grid/
root.mainloop()
