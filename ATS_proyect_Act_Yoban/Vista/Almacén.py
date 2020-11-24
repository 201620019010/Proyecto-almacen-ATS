from tkinter import *
import tkinter as tk
from tkinter import *
import pymysql
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image

# Connect to database
try:
    conexion = pymysql.connect(host='localhost',
                            user='root',
                            password='zaxQGI94',
                            db='mydb')
    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

def Inicio_Administrador():
    ventana_Inicio_Administrador = tk.Toplevel(ventana)
    ventana_Inicio_Administrador.title("Inicio Administrador")
    tk.Label(ventana_Inicio_Administrador, text="Inicio Administrador",
             font=("Agency FB", 60)).place(x=170, y=80)
    tk.Button(ventana_Inicio_Administrador, text = 'Iniciar Sesión',font=("Agency FB",14), command = iniciar ,width=20) .place(x=200,y=300)
    tk.Button(ventana_Inicio_Administrador, text = 'Consultar',font=("Agency FB",14),width=20) .place(x=200,y=500)

    #Imagen inicio de sesión
    ventana_Inicio_Administrador.geometry("800x800")
    Imagen_Inicio_Sesión = PhotoImage(file='iniciar sesión.png')
    Label_Imagen_Inicio_Sesión = Label(ventana_Inicio_Administrador,image=Imagen_Inicio_Sesión, width=150, height=150) .place(x=400,y=250)
    
    #Imagen consultar
    ventana_Inicio_Administrador.geometry("800x800")
    Imagen_Consultar = PhotoImage(file='consultar.png')
    Label_Imagen_Consultar = Label(ventana_Inicio_Administrador,image=Imagen_Consultar, width=150, height=150) .place(x=400,y=450)


    ventana_Inicio_Administrador.mainloop()
   

def Menú_Almacenista():
    ventana_Menú_Almacenista = tk.Toplevel(ventana)
    ventana_Menú_Almacenista.title("Menú Almacenista")
    tk.Label(ventana_Menú_Almacenista, text="Menú Almacenista",
             font=("Agency FB", 60)).place(x=170, y=80)
    tk.Button(ventana_Menú_Almacenista, text = 'Prestar',font=("Agency FB",14),width=20) .place(x=200,y=350)
    tk.Button(ventana_Menú_Almacenista, text = 'Consultar',font=("Agency FB",14),width=20) .place(x=200,y=530)
    #Imagen Prestar
    ventana_Menú_Almacenista.geometry("800x800")
    Imagen_Prestar = PhotoImage(file='prestar.png')
    Label_Imagen_Prestar = Label(ventana_Menú_Almacenista,image=Imagen_Prestar, width=150, height=150) .place(x=450,y=300)
    
    #imagen consultar
    ventana_Menú_Almacenista.geometry("800x800")
    Imagen_Consultar = PhotoImage(file='consultar2.png')
    Label_Imagen_Consultar = Label(ventana_Menú_Almacenista,image=Imagen_Consultar, width=150, height=214) .place(x=450,y=450)

    ventana_Menú_Almacenista.mainloop()


def Menú_Administrador():
    ventana_Menú_Administrador = tk.Toplevel(ventana)
    ventana_Menú_Administrador.title("Menú Administrador")
    tk.Label(ventana_Menú_Administrador, text="Menú Administrador",
             font=("Agency FB", 60)).place(x=550, y=80)
    tk.Button(ventana_Menú_Administrador, text = 'Registrar',font=("Agency FB",14),width=20) .place(x=100,y=350)
    tk.Button(ventana_Menú_Administrador, text = 'Consultar',font=("Agency FB",14),width=20) .place(x=100,y=600)
    tk.Button(ventana_Menú_Administrador, text = 'Modificar',font=("Agency FB",14),width=20) .place(x=100,y=350)

    #Imagen Registrar
    ventana_Menú_Administrador.geometry("800x800")
    Imagen_Registrar = PhotoImage(file='registrar.png')
    Label_Imagen_Registrar = Label(ventana_Menú_Administrador,image=Imagen_Registrar, width=150, height=150) .place(x=100,y=300)
    
    #Imagen Consultar
    ventana_Menú_Administrador.geometry("800x800")
    Imagen_Consultar = PhotoImage(file='consultar.png')
    Label_Imagen_Consultar = Label(ventana_Inicio_Administrador,image=Imagen_Consultar, width=150, height=214) .place(x=150,y=500)

    #Imagen Modificar
    ventana_Menú_Almacenista.geometry("800x800")
    Imagen_Modificar = PhotoImage(file='modificar.png')
    Label_Imagen_Modificar = Label(ventana_Inicio_Administrador,image=Imagen_Modificar, width=150, height=214) .place(x=100,y=500)

    ventana_Menú_Administrador.mainloop()


def iniciar():

    def login(): 
        usuario = caja1.get()
        contraseña = caja2.get()

        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM Login WHERE username = %s AND password = %s;"
                cursor.execute(consulta, (usuario, contraseña))
                cursor.fetchone()

                registrarMateriales()

                conexion.commit()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            MessageBox.showinfo(title = "Login Incorrecto", message = "Usuario o contraseña Incorrectos")   
    
    ventana_Iniciar = tk.Toplevel(ventana)
    ventana_Iniciar.title("Bienvenido. Ingrese a la plataforma ATS...")

 

    tk.Button(ventana_Iniciar, text = "Registrese", font= ("Agency FB", 14), command = registrar).place(x=345,y=650)
    tk.Button(ventana_Iniciar, text = "Salir", font = ("Agency FB", 14), command = ventana.destroy).place(x=0,y=0) 

    #imagen Iniciar
    ventana_Iniciar.geometry("800x800")
    Imagen_Iniciar = PhotoImage(file='icono2.png')
    Label(ventana_Iniciar,image=Imagen_Iniciar).place(x=100,y=-10)
    tk.Button(ventana_Iniciar, text = 'Login', font = ("Agency FB",14), command = login).place(x=365,y=555)

    Label(ventana_Iniciar, text = "Usuario:", font= ("Agency FB", 14),fg="Black").place(x=280,y=490)
    caja1 = Entry(ventana_Iniciar)
    caja1.place(x=250,y=525)

    Label(ventana_Iniciar, text = "Contraseña:", font= ("Agency FB", 14)).place(x=430,y=490)
    caja2 = Entry(ventana_Iniciar, show = "*")
    caja2.place(x=410,y=525)

    Label(ventana_Iniciar, text = "LogIn:", font= ("Agency FB", 60),fg="Black").place(x=310,y=0)
    Label(ventana_Iniciar, text = "¿No está registrado?", font= ("Agency FB", 14)).place(x=315,y=620)

    ventana_Iniciar.mainloop()

    
def registrar():

    def registrarLog():
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM login"
        )

        username = caja1.get()
        password = caja2.get()
        fechaCreacion = caja3.get()

        cursor.execute(
            "INSERT INTO login VALUES (%s, %s, %s)",
            (username, password, fechaCreacion)
        )
        MessageBox.showinfo(title = "Usuario Registrado", message = "Su usuario ha sido creado")
        conexion.commit()
        conexion.close()

    ventana_Registrar = tk.Toplevel(ventana)
    ventana_Registrar.title ("Bienvenido. Por favor ingrese sus datos.")

    ventana_Registrar.geometry("800x800") 
    Imagen_Registrar = PhotoImage(file='icono.png')
    Label(ventana_Registrar,image = Imagen_Registrar).place(x=205,y=90)
    tk.Button(ventana_Registrar, text = 'Registrar', font = ("Agency FB",14), command = registrarLog).place(x=350,y=600)
    tk.Button(ventana_Registrar, text = 'Salir', font = ("Agency FB",14), command = ventana.destroy).place(x=0,y=10)

    Label(ventana_Registrar, text = "Usuario:", font= ("Agency FB", 14),fg="Black").place(x=198,y=505)
    caja1 = Entry(ventana_Registrar)
    caja1.place(x=160,y=538)

    Label(ventana_Registrar, text = "Contraseña:", font= ("Agency FB", 14)).place(x=358,y=505)
    caja2 = Entry(ventana_Registrar, show = "*")
    caja2.place(x=338,y=538)

    Label(ventana_Registrar, text = "Fecha Creacion:", font= ("Agency FB", 14)).place(x=518,y=505)
    caja3 = Entry(ventana_Registrar)
    caja3.place(x=508,y=538)

    Label(ventana_Registrar, text = "Registro:", font= ("Agency FB", 60),fg="Black").place(x=300,y=-10)

    ventana_Registrar.mainloop()

def registrarMateriales():
    ventana_RegistrarMater = tk.Toplevel(ventana)
    ventana_RegistrarMater.title ("Bienvenido. Por favor ingrese sus datos.")

    ventana_RegistrarMater.geometry("800x800") 
    Imagen_Registrar = PhotoImage(file='registro.png')
    Label(ventana_RegistrarMater,image = Imagen_Registrar).place(x=205,y=90)
    tk.Button(ventana_RegistrarMater, text = 'Usuarios', font = ("Agency FB",14),command = usuarios).place(x=300,y=390)
    tk.Button(ventana_RegistrarMater, text = 'Insumos', font = ("Agency FB",14),command = insumos ).place(x=460,y=390)
    tk.Button(ventana_RegistrarMater, text = 'Herramientas', font = ("Agency FB",14),command = herramientas).place(x=300,y=300)
    tk.Button(ventana_RegistrarMater, text = '    EPP    ', font = ("Agency FB",14),command = epp ).place(x=460,y=300)
    tk.Button(ventana_RegistrarMater, text = '   Salir   ', font = ("Agency FB",14),command = ventana.destroy ).place(x=300,y=470)

    Label(ventana_RegistrarMater, text = "Registrar Artículos:", font= ("Agency FB", 60),fg="Black").place(x=180,y=-10)
    ventana_RegistrarMater.mainloop()

def usuarios():
    ventana_Usuarios = tk.Toplevel(ventana)
    ventana_Usuarios.title ("Bienvenido. Por favor ingrese sus datos.")
    ventana_Usuarios.geometry("800x800") 

    def insertarUsuario():
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM Usuario"
        )

        Label(ventana_Usuarios, text = "Registrar Usuarios:", font= ("Agency FB", 60),fg="Black").place(x=180,y=0)
        Label(ventana_Usuarios, text = "Por favor llene los campos", font= ("Agency FB", 14)).place(x=315,y=620)

        Label(ventana_Usuarios, text = "Cédula:", font= ("Agency FB", 14)).place(x=240,y=200)
        cedula = Entry(ventana_Usuarios)
        cedula.place(x=440,y=200)
        Label(ventana_Usuarios, text = "Nombre del Usuario:", font= ("Agency FB", 14)).place(x=240,y=300)
        nombreUsuario = Entry(ventana_Usuarios)
        nombreUsuario.place(x=440,y=300)
        Label(ventana_Usuarios, text = "Fecha de Registro:", font= ("Agency FB", 14)).place(x=240,y=400)
        fechaRegistro = Entry(ventana_Usuarios)
        fechaRegistro.place(x=440,y=400)
        tk.Button(ventana_Usuarios, text = 'Guardar', font = ("Agency FB",14),command = insertarUsuario).place(x=380,y=500)  
        cursor.execute(
            "INSERT INTO Usuario VALUES (%s, %s, %s)",
            (cedula, nombreUsuario, fechaRegistro)
        )

        conexion.commit()
        conexion.close() 
    
    insertarUsuario()
    ventana_Usuarios.mainloop()

def insumos():
    print("")

def herramientas():
    print("")

def epp():
    print("")


ventana = Tk()
ventana.title ("Almacen ATS")
             
#Titulo Bienvenido
Titulo_Bienvenido = Label(ventana, text = 'Bienvenido',font=("Agency FB", 60)) .place(x=200,y=80)

#Titulo Inicio
Titulo_Inicio = Label(ventana, text = 'Inicio',font=("Agency FB", 40)) .place(x=386,y=200)

#Titulo Seleccione una opción
Titulo_Seleccione_Una_Opción = Label(ventana, text = 'Seleccione una opción',font=("Agency FB", 20)) .place(x=340,y=280)

#Botón Administrador
Boton_Administrador = Button(ventana, text = 'Administrador',command = Inicio_Administrador, font=("Agency FB",14),width=20) .place(x=200,y=600)

#Botón Almacenista
Boton_Almacenista =   Button(ventana, text = 'Almacenista',command = Menú_Almacenista, font=("Agency FB",14),width=20) .place(x=480,y=600)

#Imagen inicio
ventana.geometry("800x800")
Imagen_Inicio = PhotoImage(file='inicio.png')
Label_Imagen_Inicio = Label(ventana,image=Imagen_Inicio, width=100, height=110) .place(x=550,y=80)

#Imagen Administrador
ventana.geometry("800x800")
Imagen_Administrador = PhotoImage(file='Administrador.png')
Label_Imagen_Inicio = Label(ventana,image=Imagen_Administrador, width=150, height=220) .place(x=200,y=350)

#Imagen Almacenista
ventana.geometry("800x800")
Imagen_Almacenista = PhotoImage(file='Almacenista.png')
Label_Imagen_Inicio = Label(ventana,image=Imagen_Almacenista, width=150, height=220) .place(x=480,y=350)

ventana.mainloop()