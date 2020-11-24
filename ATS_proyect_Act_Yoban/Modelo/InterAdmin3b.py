from tkinter import *

raiz= Tk()
raiz.title("Registrar EPP")
raiz.iconbitmap(r"D:\SantiagoToro\Documentos\ProgramacionVS\Ejemplos Python\.vscode\Logo.ico")
raiz.config (bg = "green")

miframe =Frame(raiz)
miframe.pack()
miframe.config(bg= "yellow", width=500,height=150) 

cuadroCodigo = Entry(miframe)
cuadroCodigo.grid(row=0, column=1)
miLabel =Label(miframe, text= "Ingrese codigo EPP: ").grid(row=0, column=0)

cuadroNombre = Entry(miframe)
cuadroNombre.grid(row=1, column=1)
miLabel =Label(miframe, text= "Ingrese nomrbre EPP: ").grid(row=1, column=0)

cuadroCantidad = Entry(miframe)
cuadroCantidad.grid(row=2, column=1)
miLabel =Label(miframe, text= "Ingrese cantidad EPP: ").grid(row=2, column=0)

Button(miframe, text="Agregar nuevo EPP").grid() 
Button(miframe, text="Regresar").grid()  

raiz.mainloop()