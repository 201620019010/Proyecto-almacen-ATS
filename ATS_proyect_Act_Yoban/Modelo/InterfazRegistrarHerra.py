from tkinter import *
import pymysql
from tkinter import messagebox as MessageBox
#from PIL import ImageTk, Image

# Connect to database

try:

    conexion = pymysql.connect(host='localhost',

                            user='root',

                            password='2421',

                            db='mydb')

    print("Conexión correcta")

except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

    print("Ocurrió un error al conectar: ", e)



ventana = Tk()
ventana.title ("Almacen ATS. Bienvenido...")


image2 = Image.open("fondo1.jpg") 
image1 = ImageTk.PhotoImage(image2)  

ventana.geometry("800x800") 



Label(ventana, image=image1).place(x=-1,y=0)




Label(ventana, text = "Usuario:", font= ("Daytona", 12),fg="Black", bg="white",).place(x=185,y=469)

caja1 = Entry(ventana)

caja1.place(x=160,y=500)



Label(ventana, text = "Contraseña:", font= ("Daytona", 12)).place(x=348,y=469)

caja2 = Entry(ventana, show = "*")

caja2.place(x=330,y=500)



Label(ventana, text = "Fecha Creacion:", font= ("Daytona", 12)).place(x=500,y=469)

caja3 = Entry(ventana)

caja3.place(x=500,y=500)



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

    

Button (text = "Registrar", font= ("Daytona", 11), command = registrarLog).place(x=350,y=600)

ventana.mainloop()