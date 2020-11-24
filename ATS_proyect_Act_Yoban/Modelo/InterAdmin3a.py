from tkinter import *

raiz= Tk()
raiz.title("Registrar herramienta")
raiz.iconbitmap(r"D:\SantiagoToro\Documentos\ProgramacionVS\Ejemplos Python\.vscode\Logo.ico")
raiz.config (bg = "green")

miframe =Frame(raiz)
miframe.pack()
miframe.config(bg= "yellow", width=500,height=150) 


cuadroHerramienta = Entry(miframe)
cuadroHerramienta.grid(row=0, column=1)
miLabel =Label(miframe, text= "Ingrese nombre herramienta: ").grid(row=0, column=0)

cuadroCodiHerramienta = Entry(miframe)
cuadroCodiHerramienta.grid(row=1, column=1)
miLabel =Label(miframe, text= "Ingrese codigo herramienta: ").grid(row=1, column=0)

CuadroDescripcion = Entry(miframe)
CuadroDescripcion.grid(row=2, column=1)
miLabel =Label(miframe, text= "Ingrese descripcion herramienta: ").grid(row=2, column=0)

CuadroMarca = Entry(miframe)
CuadroMarca.grid(row=3, column=1)
miLabel =Label(miframe, text= "Ingrese marca de la herramienta: ").grid(row=3, column=0)

cuadroUbicacion = Entry(miframe)
cuadroUbicacion.grid(row=4, column=1)
miLabel =Label(miframe, text= "Ingrese ubicacion de la herramienta en el almacen: ").grid(row=4, column=0)

Button(miframe, text="Agregar nueva herramienta").grid() 
Button(miframe, text="Regresar").grid()  


raiz.mainloop()