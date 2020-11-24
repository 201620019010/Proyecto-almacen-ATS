from tkinter import *

raiz= Tk()
raiz.title("Perfil Administrador - Modificar.")
raiz.iconbitmap(r"D:\SantiagoToro\Documentos\ProgramacionVS\Ejemplos Python\.vscode\Logo.ico")
raiz.config (bg = "green")

miframe =Frame()
miframe.pack()
miframe.config(bg= "yellow") 
miframe.config(width="800", height="400")
miLabel =Label(miframe, text= "¿Que deseas modificar?")
miLabel.pack()

Button(miframe, text="Modificar insumos.").pack()  
Button(miframe, text="Modificar EPP.").pack() 
Button(miframe, text="Modificar herramienta.").pack() 
Button(miframe, text ="Regresar.").pack()
raiz.mainloop()