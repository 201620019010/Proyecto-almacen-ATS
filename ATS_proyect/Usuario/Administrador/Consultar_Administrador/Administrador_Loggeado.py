from Registrar.Registrar import insertarUsuario

def Menu_Administrador_Loggeado():
    print("Bienvenido, seleccione una opción")
    print()
    print("[7] Registrar")
    print("[8] Modificar")
    alternativa = input()
    
    if(alternativa == 7):
        print(insertarUsuario())

    if(alternativa == 8):
        print("")