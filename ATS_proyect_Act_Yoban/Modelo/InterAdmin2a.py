from tkinter import *

raiz= Tk()
raiz.title("Perfil Administrador")
raiz.iconbitmap(r"logo.ico")
raiz.config (bg = "green")

miframe =Frame()
miframe.pack()
miframe.config(bg= "yellow") 
miframe.config(width="800", height="400")
miLabel =Label(miframe, text= "¿ Que deseas registrar ?")
miLabel.pack()

Button(miframe, text="Registrar insumos.").pack()  
Button(miframe, text="Registrar EPP.").pack() 
Button(miframe, text="Registrar herramienta.").pack() 
raiz.mainloop()