# Connect to database
from tkinter import *
import pymysql
from tkinter import messagebox as MessageBox
from Interfaz_Registrar import *

try:
    conexion = pymysql.connect(host='localhost',
                            user='root',
                            password='2421',
                            db='mydb')
    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

ventana = Tk()
ventana.title ("Bienvenido. Ingrese a la plataforma ATS...")

ventana.geometry("800x800") 

image4 = Image.open("icono2.png") 
image3 = ImageTk.PhotoImage(image4) 
Label(ventana, image=image3).place(x=100,y=-20)

Label(ventana, text = "Usuario:", font= ("Daytona", 12),fg="Black", bg="white").place(x=280,y=490)
caja1 = Entry(ventana)
caja1.place(x=250,y=510)

Label(ventana, text = "Contraseña:", font= ("Daytona", 12)).place(x=430,y=490)
caja2 = Entry(ventana, show = "*")
caja2.place(x=410,y=510)

Label(ventana, text = "LogIn:", font= ("Arial Black", 15),fg="Black", bg="white",).place(x=358,y=17)

def login(): 
    usuario = caja1.get()
    contraseña = caja2.get()

    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM Login WHERE username = %s AND password = %s;"
            cursor.execute(consulta, (usuario, contraseña))
            cursor.fetchone()
            MessageBox.showinfo(title = "Login Correcto", message = "Usuario y contraseña correctos")
            conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        MessageBox.showinfo(title = "Login Incorrecto", message = "Usuario o contraseña Incorrectos")   

Button (text = "Login", font= ("Daytona", 11), command = registrarLog).place(x=365,y=580)

Label(ventana, text = "¿No está registrado?", font= ("Daytona", 11)).place(x=315,y=650)

Button (text = "Registrese", font= ("Daytona", 11), command = registrarLog).place(x=345,y=700)

ventana.mainloop()