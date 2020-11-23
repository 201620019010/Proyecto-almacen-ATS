from Administrador.Iniciar_Sesion.Iniciar_Sesion import Acceder
from Administrador.Consultar_Administrador.Administrador_Loggeado import Menu_Administrador_Loggeado
from Almacenista.Consultar_Almacenista import Consultar_Almacenista
from Almacenista.Entregar.Entregar import Entregas

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
    
    if(respuesta == 3):
        print(Acceder())

    if(respuesta == 4):
        print(Menu_Administrador_Loggeado())

def Inicio_Almacenista():

    print("[5] Consultar")
    print("[6] Entregar")
    eleccion = int(input("Ingrese un valor: "))
    
    if(eleccion == 5):
        print(Consultar_Almacenista())

    if(eleccion == 6):
        print(Entregas())

Inicio()