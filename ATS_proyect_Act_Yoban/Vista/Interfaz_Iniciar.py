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

def iniciar():
    ventana = Tk()
    ventana.title("Bienvenido. Ingrese a la plataforma ATS...")

    ventana.geometry("800x800") 

    image4 = Image.open("icono2.png") 
    image3 = ImageTk.PhotoImage(image4) 
    Label(ventana, image=image3).place(x=100,y=-10)

    Label(ventana, text = "Usuario:", font= ("Agency FB", 14),fg="Black").place(x=280,y=490)
    caja1 = Entry(ventana)
    caja1.place(x=250,y=525)

    Label(ventana, text = "Contraseña:", font= ("Agency FB", 14)).place(x=430,y=490)
    caja2 = Entry(ventana, show = "*")
    caja2.place(x=410,y=525)

    Label(ventana, text = "LogIn:", font= ("Agency FB", 60),fg="Black").place(x=310,y=0)

    def login(): 
        usuario = caja1.get()
        contraseña = caja2.get()

        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM Login WHERE username = %s AND password = %s;"
                cursor.execute(consulta, (usuario, contraseña))
                cursor.fetchone()

                #MessageBox.showinfo(title = "Login Correcto", message = "Usuario y contraseña correctos")

                conexion.commit()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            MessageBox.showinfo(title = "Login Incorrecto", message = "Usuario o contraseña Incorrectos")   

    Button (text = "Login", font= ("Agency FB", 14), command = login).place(x=365,y=550)

    Label(ventana, text = "¿No está registrado?", font= ("Agency FB", 14)).place(x=315,y=620)
    Button (text = "Registrese", font= ("Agency FB", 14), command = registrar1).place(x=345,y=650)
    Button (text = "Salir", font= ("Agency FB", 14), command = ventana.destroy).place(x=0,y=10)
    ventana.mainloop()

def registrar1():
    ventana = Tk()
    ventana.title("Bienvenido. Por favor ingrese sus datos.")

    ventana.geometry("800x800") 

    image4 = Image.open("icono.png") 
    image3 = ImageTk.PhotoImage(image4) 
    Label(ventana, image=image3).place(x=205,y=90)

    Label(ventana, text = "Usuario:", font= ("Agency FB", 14),fg="Black").place(x=198,y=505)
    caja1 = Entry(ventana)
    caja1.place(x=160,y=538)

    Label(ventana, text = "Contraseña:", font= ("Agency FB", 14)).place(x=358,y=505)
    caja2 = Entry(ventana, show = "*")
    caja2.place(x=338,y=538)

    Label(ventana, text = "Fecha Creacion:", font= ("Agency FB", 14)).place(x=518,y=505)
    caja3 = Entry(ventana)
    caja3.place(x=508,y=538)

    Label(ventana, text = "Registro:", font= ("Agency FB", 60),fg="Black").place(x=300,y=-10)

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
        
    Button (text = "Registrar", font= ("Agency FB", 14), command = registrarLog).place(x=350,y=600)
    Button (text = "Salir", font= ("Agency FB", 14), command = ventana.destroy).place(x=0,y=10)
    ventana.mainloop()

iniciar()