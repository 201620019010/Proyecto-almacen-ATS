from tkinter import *

raiz= Tk()
raiz.title("Perfil Administrador")
#raiz.geometry("350x350")
raiz.iconbitmap(r"D:\SantiagoToro\Documentos\ProgramacionVS\Ejemplos Python\.vscode\Logo.ico")
raiz.config (bg = "green")

#creamos un objeto frame
miframe =Frame()
#empaquetado del frame al main
miframe.pack()
#cambiar caracteristicas
miframe.config(bg= "yellow") 
miframe.config(width="650", height="400")

#loop principañ
raiz.mainloop()