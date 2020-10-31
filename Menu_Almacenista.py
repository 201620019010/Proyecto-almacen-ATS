def Inicio_Almacenista():
    print("Bienvenido, seleccione una opción")
    print()
    print("[5] Consultar")
    print("[6] Entregar")
    eleccion = input()
    instancia5 = Consultar_Almacenista()
    instancia6 = Entregar()
    if(eleccion == 5):
        instancia5

    if(eleccion == 6):
        instancia6