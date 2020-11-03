# menu de registro
import pymysql

try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='zaxQGI94',
                             db='mydb')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

print("MENU:\n 1.Nuevo Empleado\n 2.Nueva Herramienta.\n 3.Nuevo Insumo.\n 4.Nuevo Epp.\n ")

opcion = int(input("Elige una opcion: "))

def insertarUsuario():
    print ("Nuevo empleado")

    cursor = conexion.cursor()
    cursor.execute(
        "SELECT * FROM Usuario"
    )

    cedula = input("Cedula: ")
    nombreUsuario = input("Nombre: ")
    fechaRegistro =input ("Fecha registro: ")

    cursor.execute(
        "INSERT INTO Usuario VALUES (%s, %s, %s)",
        (cedula, nombreUsuario, fechaRegistro)
    )

    conexion.commit()
    conexion.close()  

    print ("Se ha creado: " ,nombreUsuario ,", con cedula:", cedula)

def insertarHerramienta():
    print ("Nueva herramienta")

    cursor = conexion.cursor()
    cursor.execute(
        "SELECT * FROM Herramientas"
    )
        
    codHerramienta = input("Codigo herramienta: ")    
    nombre = input("Nombre herramienta: ")
    tipoHerramienta = input("Tipo de herramienta: ")
    ubicacion = input("Ubicación de la herramienta: ")
    disponibilidad =  input("Disponibilidad de herramienta: ")
    unidadesDisponibles = input("Unidades Disponibles: ")

    cursor.execute(
        "INSERT INTO Herramientas VALUES (%s, %s, %s, %s, %s, %s)",
        (codHerramienta, nombre, tipoHerramienta, ubicacion,disponibilidad,unidadesDisponibles)
    )

    conexion.commit()
    conexion.close()  

    print ("Se ha registrado una herramienta con codigo: " ,codHerramienta,", de nombre: ",nombre,", tipo de herramienta", tipoHerramienta)
    print(" ubicada en: ",ubicacion," con (1 disponible, 0 no disponible): ",disponibilidad,", y las unidades disponibles son: ",unidadesDisponibles)

def insertarInsumo():
    print ("Nuevo insumo")
    
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT * FROM Insumos")

    codInsumos = input("Codigo Insumo: ")
    nombre = input("Nombre Insumo: ")
    ubicacion = input ("Ubicacion: ")
    disponibilidad = input("Disponibilidad: ")
    unidadesDisponibles = input("Unidades Disponibles: ")  

    cursor.execute(
        "INSERT INTO Insumos VALUES (%s, %s, %s, %s, %s)",
        (codInsumos,nombre,ubicacion,disponibilidad,unidadesDisponibles)
    )

    conexion.commit()
    conexion.close()

    print("Se ha creado un nuevo insumo con codigo: ",codInsumos,", con nombre: ",nombre,", con ubicacion en: ",ubicacion)
    print("con disponibilidad de: ",disponibilidad,", con unidades disponibles de: ",unidadesDisponibles)

def insertarEpp():
    print ("Nuevo EPP")

    cursor = conexion.cursor()
    cursor.execute(
        "SELECT * FROM EPP")
   
        
    codEPP = input ("Codigo EPP: ")
    nombre = input("Nombre EPP: ")
    ubicacion = input("Ubicacion en el almacen: ")
    disponibilidad = input("Disponibilidad: ")
    unidadesDisponibles = input("Unidades Disponibles: ")

    cursor.execute(
        "INSERT INTO  EPP VALUES (%s, %s, %s, %s, %s)",
        (codEPP,nombre,ubicacion,disponibilidad,unidadesDisponibles)
    )
        
    conexion.commit()
    conexion.close()  

    print("Se ha registrado un nuevo EPP con codigo: ",codEPP,", con nombre: ",nombre,", con ubicacion en: ",ubicacion)
    print("con disponibilidad de: ",disponibilidad,", con unidades disponibles de: ",unidadesDisponibles)

if opcion == 1:
    insertarUsuario()
elif opcion == 2:
    insertarHerramienta()
elif opcion == 3:
    insertarInsumo()
elif opcion == 4: 
    insertarEpp()
else:
    print("¡Ingresó un valor incorrecto!")

print("***Ejecución finalizada***")

                