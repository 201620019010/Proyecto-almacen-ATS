from tkinter import *

def funcion():
      Otraventana.state(newstate = "normal")
      raiz.state(newstate = "withdraw")

def funcion2():
      Otraventana.state(newstate = "withdraw")
      raiz.state(newstate = "normal") #state(newstate = "withdraw")root.deiconify, zoomed()


raiz= Tk()
raiz.state(newstate = "normal")
raiz.title("Perfil Almacenista")
raiz.geometry("250x150+300+100")
raiz.iconbitmap(r"D:\SantiagoToro\Documentos\ProgramacionVS\Ejemplos Python\.vscode\Logo.ico")
raiz.config (bg = "green")

Otraventana = Button(raiz, text="Regresar inicio", bg="blue", font= ("Times New Roman", 12), fg="yellow", command=funcion)
Otraventana.pack()


#creamos un objeto frame
miframe =Frame()
#empaquetado del frame al main
miframe.pack()
#cambiar caracteristicas
miframe.config(bg= "yellow") 
miframe.config(width="800", height="400")


miLabel = Label(miframe, text= "Bienvenido Almacenista")
miLabel.pack()
miLabel = Label(miframe, text= "¿ Que desea hacer ?")
miLabel.pack()

Button(miframe, text="Consultar").pack()  
Button(miframe, text="Prestar herramienta").pack() 
Button(miframe, text="Entrega Consumibles").pack()

#loop principal
raiz.mainloop()