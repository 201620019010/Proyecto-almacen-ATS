def Menu_Administrador_Loggeado:
    print("Bienvenido, seleccione una opción")
    print()
    print("[7] Registrar")
    print("[8] Modificar")
    alternativa = input()
    instancia7 = Registrar()
    instancia8 = Modificar()
    if(alternativa == 7):
        instancia7

    if(alternativa == 8):
        instancia8