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

def registrar():
    ventana = Tk()
    ventana.title ("Bienvenido. Por favor ingrese sus datos.")

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

registrar()
