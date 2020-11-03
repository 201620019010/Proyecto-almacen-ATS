import pymysql
from Consultar_Administrador.Administrador_Loggeado import Menu_Administrador_Loggeado

def Acceder():

    usuario = input("Ingresar Usuario: ")
    contraseña = input("Ingresar Contraseña: ")

    try:
        conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='zaxQGI94',
                                db='mydb')
        print("Conexión correcta")

        try:
            with conexion.cursor() as cursor:
            
                consulta = "SELECT * FROM Login WHERE username = %s AND password = %s;"
                cursor.execute(consulta, (usuario, contraseña))
                print(Menu_Administrador_Loggeado())
                result = cursor.fetchone()
                print(result)
                conexion.commit()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Usuario o contraseña no válido")

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

    finally: 
        conexion.close()   

Acceder()