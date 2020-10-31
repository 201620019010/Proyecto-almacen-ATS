def Menu_Modificar():
    print("Seleccione cual opción quiere modificar")
    print()
    print("[1] Empleado")
    print("[2] Herramientas")
    print("[3] Insumos")
    print("[4] EPP")
    opcion = input()
    instancia = Modificar()

    if(opcion == 1):
        instancia.Modificar_Empleado()

    if(opcion == 2):
        instancia.Modificar_Herramientas()

    if(opcion == 3):
        instancia.Modificar_Insumos()

    if(opcion == 4):
        instancia.Modificar_EPP()


def Modificar_Empleado():



def Modificar_Herramientas():



def Modificar_Insumos():



def Modificar_EPP():
