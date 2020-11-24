from tkinter import *

raiz= Tk()
raiz.title("Perfil Administrador")
#raiz.geometry("350x350")
raiz.iconbitmap("Logo.ico")
raiz.config (bg = "green")

#creamos un objeto frame
miframe =Frame()
#empaquetado del frame al main
miframe.pack()
#cambiar caracteristicas
miframe.config(bg= "yellow") 
miframe.config(width="800", height="400")


miLabel = Label(miframe, text= "Bienvenido Administrador")
miLabel.pack()
miLabel = Label(miframe, text= "¿ Que desea hacer ?")
miLabel.pack()

Button(miframe, text="Registrar").pack()  
Button(miframe, text="Modificar").pack() 


#loop principal
raiz.mainloop()