import pymysql

try:
    conexion = pymysql.connect(host='localhost',
                            user='root',
                            password='zaxQGI94',
                            db='mydb')
    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

#Lista es el elemento que queramos buscar en nuestra base de datos
#Esto se hace utilizando un algoritmo de búsqueda lineal para la base de datos.

target = 0
lista=[]

def Inicio():
    print("Bienvenido, seleccione una opción")
    print()
    print("[1] Acceder como Administrador")
    print("[2] Acceder como Almacenista")
    opcion = input("Ingrese un valor: ")
    instancia1 = ConsultarAdministrador()
    instancia2 = ConsultarAlmacenista()
    if(opcion == 1):
        instancia1

    if(opcion == 2):
        instancia2

def ConsultarAlmacenista(elementos,target):
        for i in range(len(elementos)):
            if elementos[i] == target:
                return i
        print("No se encontró el elemento solicitado por el usuario")


def ConsultarAdministrador(query=''):
    #Acá serían los objetos que necesitamos para nuestra ejecución.
    datos = [Administrador, Usuario, Objeto, Empleado]

    conn = MySQLdb.connect(*datos)  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    cursor.execute(query)  # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Traer los resultados de un select
    else:
        conn.commit()  # Hacer efectiva la escritura de datos
        data = None

    cursor.close()  # Cerrar el cursor
    conn.close()  # Cerrar la conexión

    return data

Inicio()

