import  tkinter as tk
from  tkinter import ttk
vent = tk.Tk()
vent.title("probando Entry")
vent.geometry("600x400")
vent.iconbitmap("proyecto/favicon.ico")


#Creando botones
btn1 = ttk.Button(vent, text = "Botón one")
btn1.grid(row=0, column=1, sticky="NSWE")


txt1 = ttk.Entry(vent,width=20, justify=tk.CENTER ) #width es la cantidad de caracteres que soporta el input show="*"
txt1.grid(row=0, column=0)

txt1.insert(0,"Intr solo numeros") # hace las veces del placeholder
txt1.insert(tk.END,".") #permite poner un dato al final del texto

txt2 = ttk.Entry(vent,width=20, justify=tk.CENTER, ) #state=tk.DISABLED no deja ver los datos del input
txt2.grid(row=1, column=0)

txt2.insert(0,"Solo lectura") # hace las veces del placeholder
txt2.insert(tk.END,".") #permite poner un dato al final del texto
# txt2.config(state="readonly")




def enviar():
    print (txt2.get())

btn2 = ttk.Button(vent, text= "Enviar", command=enviar)
btn2.grid(row=1,column=1)
txt2.delete(0, tk.END)
txt2.select_range(0, tk.END)
txt1.focus()

vent.mainloop()