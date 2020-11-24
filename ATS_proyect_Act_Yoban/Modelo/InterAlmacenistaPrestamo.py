from tkinter import *

raiz= Tk()
raiz.title("Perfil Almacenista")
#raiz.geometry("350x350")
raiz.iconbitmap(r"D:\SantiagoToro\Documentos\ProgramacionVS\Ejemplos Python\.vscode\Logo.ico")
raiz.config (bg = "green")

miframe =Frame()
miframe.pack()
miframe.config(bg= "yellow") 
miframe.config(width="800", height="400")

miLabel = Label(miframe, text= "ingresar datos del prestamo")
miLabel.grid(row=0, column=0)

cuadroCodigo = Entry(miframe)
cuadroCodigo.grid(row=1, column=1)
miLabel =Label(miframe, text= "Ingrese codigo insumo: ").grid(row=1, column=0)


raiz.mainloop()