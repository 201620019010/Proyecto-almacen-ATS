from tkinter import ttk
from tkinter import *


class Inicio_Aplicación:

    def __init__(self,ventana):
        self.wind = ventana
        self.wind.title('Almacén ATS')

        #Titulo Bienvenido
        Titulo_Bienvenido = Label(ventana, text = 'Bienvenido',font=("Agency FB", 60)) .place(x=670,y=80)

        #Titulo Inicio
        Titulo_Inicio = Label(ventana, text = 'Inicio',font=("Agency FB", 40)) .place(x=670,y=200)

        #Titulo Seleccione una opción
        Titulo_Seleccione_Una_Opción = Label(ventana, text = 'Seleccione una opción',font=("Agency FB", 20)) .place(x=670,y=300)

        #Botón Administrador
        Boton_Administrador = Button(ventana, text = 'Administrador', font=("Agency FB",14),width=20) .place(x=600,y=400)

        #Botón Almacenista
        Boton_Almacenista =   Button(ventana, text = 'Almacenista',font=("Agency FB",14),width=20) .place(x=800,y=400)

    

if __name__ == "__main__":
    ventana = Tk()
    Aplicación_Inicio = Inicio_Aplicación(ventana)
    #Imagen inicio
    ventana.geometry("150x150+0+0")
    ventana.config(bg="white")
    Imagen_Inicio = PhotoImage(file='inicio.png')
    Label_Imagen_Inicio = Label(ventana,image=Imagen_Inicio, width=170, height=170) .place(x=200,y=80)
 

    
    