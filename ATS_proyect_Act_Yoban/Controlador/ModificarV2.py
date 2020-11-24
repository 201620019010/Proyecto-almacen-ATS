import pymysql

def Menu_Modificar():
    print("Seleccione cual opción quiere modificar")
    print()
    print("[1] Empleado")
    print("[2] Herramientas")
    print("[3] Insumos")
    print("[4] EPP")
    opcion = input()
    instancia = ModificarV2()

    if(opcion == 1):
        instancia.Modificar_Empleado()

    if(opcion == 2):
        instancia.Modificar_Herramientas()

    if(opcion == 3):
        instancia.Modificar_Insumos()

    if(opcion == 4):
        instancia.Modificar_EPP()

def Modificar_Empleado():
    
    print("Seleccione una opción")
    print()
    print("[1] Administrador")
    print("[2] Almacenista")
    opcion = int(input("Ingrese un valor: "))

    if(opcion == 1):
        print("Ingrese la cédula")
        cedula_Administrador = input()

        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='zaxQGI94',
                                    db='mydb')
            print("Conexión correcta")

#Modificar_Empleado()

