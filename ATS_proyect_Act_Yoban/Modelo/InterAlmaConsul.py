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

miLabel = Label(miframe, text= "¿ Que desea consultar ?")
miLabel.pack()

Button(miframe, text="Disponibilidad Herramientas").pack()  
Button(miframe, text="Disponibilidad EPP").pack() 
Button(miframe, text="Disponibilidad Consumibles").pack()
raiz.mainloop()