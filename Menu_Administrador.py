def Inicio_Administrador():
    print("Bienvenido, seleccione una opción")
    print()
    print("[3] Iniciar Sesión")
    print("[4] Consultar")
    respuesta = input()
    instancia3 = Iniciar_Sesion()
    instancia4 = Consultar_Administrador()
    if(respuesta == 3):
        instancia3

    if(respuesta == 4):
        instancia4