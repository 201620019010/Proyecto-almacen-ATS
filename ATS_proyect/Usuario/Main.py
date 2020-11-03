
def Inicio():

    print("Bienvenido, seleccione una opción")
    print("[1] Acceder como Administrador")
    print("[2] Acceder como Almacenista")
    opcion = int(input("Ingrese un valor: "))

    if(opcion == 1):
        print(Inicio_Administrador())

    if(opcion == 2):
        print(Inicio_Almacenista())
        
def Inicio_Administrador():

    print("[3] Iniciar Sesión")
    print("[4] Consultar")
    respuesta = int(input("Ingrese un valor: "))
    #instancia3 = Iniciar_Sesion.Acceder()
    #instancia4 = Consultar()
    if(respuesta == 3):
        print(Iniciar_Sesion.Acceder())

    if(respuesta == 4):
        print(instancia4.ConsultarAdministrador())

def Inicio_Almacenista():

    print("[5] Consultar")
    print("[6] Entregar")
    eleccion = int(input("Ingrese un valor: "))
    instancia5 = Consultar()
    instancia6 = Entregar()
    if(eleccion == 5):
        print(instancia5.ConsultarAlmacenista())

    if(eleccion == 6):
        print(instancia6.Entregas())

Inicio()