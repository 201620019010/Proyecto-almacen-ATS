import pymysql

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
    
    print("Seleccione una opción")
    print()
    print("[1] Administrador")
    print("[2] Almacenista")
    opcion = input()

    if(opcion == 1):
        print("Ingrese la cédula")
        cedula_Administrador = input()

 

    try:
	    conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	    try:
		    with conexion.cursor() as cursor:
			
			    consulta = "SELECT cedula, nombreAdmin, fechaRegistro, username FROM Administrador WHERE cedula = cedula_Administrador;"
			    cursor.execute(consulta, (2000))

		
			    datos_Administrador = cursor.fetchall()

		
			    for Administrador in datos_Administrador:
				    print(Administrador)

                print("Seleccione una opción a modificar")
                print()
                print("[1] cedula")
                print("[2] Nombre")
                print("[3] Fecha de registro")
                opcion = input()

            if(opcion == 1):
                print("Ingrese la nueva cédula")
                nueva_cedula = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Administrador SET cedula WHERE cedula = nueva_cedula;"
			            cursor.execute(consulta, (2000))

                        datos_Administrador = cursor.fetchall()

                        for Administrador in datos_Administrador:
				                    print(Administrador)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificcación: ", e)



            if(opcion == 2):
                print("Ingrese el nuevo nombre")
                nuevo_nombre = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Administrador SET nombreAdmin WHERE nombreAdmin = nuevo_nombre;"
			            cursor.execute(consulta, (2000))

                        datos_Administrador = cursor.fetchall()

                        for Administrador in datos_Administrador:
				                    print(Administrador)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificcación: ", e)


            if(opcion == 3):
                print("Ingrese nueva fecha de registro")
                nueva_FechaRegistro = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Administrador SET fechaRegistro WHERE fechaRegistro = nueva_FechaRegistro;"
			            cursor.execute(consulta, (2000))

                        datos_Administrador = cursor.fetchall()

                        for Administrador in datos_Administrador:
				                    print(Administrador)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificcación: ", e)
   
	 finally:
		conexion.close()
	
     except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	     print("Ocurrió un error al conectar: ", e)


    if(opcion == 2):
        print("Ingrese la cédula")
        cedula_Almacenista = input()

          try:
	    conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	    try:
		with conexion.cursor() as cursor:
			
			consulta = "SELECT cedula, nombre, fechaRegistro FROM Almacenista WHERE cedula = cedula_Almacenista;"
			cursor.execute(consulta, (2000))

		
			datos_Almacenista = cursor.fetchall()

		
			for Almacenista in datos_Almacenista:
				print(Almacenista)


            print("Seleccione una opción a modificar")
            print()
            print("[1] cedula")
            print("[2] Nombre")
            print("[3] Fecha de registro")
            opcion = input()

            if(opcion == 1):
                print("Ingrese la nueva cédula")
                nueva_cedula = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Almacenista SET cedula WHERE cedula = nueva_cedula;"
			            cursor.execute(consulta, (2000))

                        datos_Almacenista = cursor.fetchall()

                        for Almacenista in datos_Almacenista:
				                    print(Almacenista)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 2):
                print("Ingrese el nuevo nombre")
                nuevo_nombre = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Almacenista SET nombre WHERE nombre = nuevo_nombre;"
			            cursor.execute(consulta, (2000))

                        datos_Almacenista = cursor.fetchall()

                        for Almacenista in datos_Almacenista:
				                    print(Almacenista)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)


            if(opcion == 3):
                print("Ingrese nueva fecha de registro")
                nueva_FechaRegistro = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Almacenista SET fechaRegistro WHERE fechaRegistro = nueva_FechaRegistro;"
			            cursor.execute(consulta, (2000))

                        datos_Almacenista = cursor.fetchall()

                        for Almacenista in datos_Almacenista:
				                    print(Almacenista)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)

            
	 finally:
		conexion.close()
	
     except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	     print("Ocurrió un error al conectar: ", e)



def Modificar_Herramientas():

    print("Ingrese el código de la herramienta")
    codigo_Herramienta = input()

    try:
	    conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	    try:
		with conexion.cursor() as cursor:
			
			consulta = "SELECT codHerramienta, tipoHerramienta, disponibilidad, ubicacion, unidadesDisponibles FROM Herramientas WHERE codHerramienta = codigo_Herramienta;"
			cursor.execute(consulta, (2000))

			datos_Herramienta = cursor.fetchall()

		
			for Herramientas in datos_Herramienta:
				print(Herramientas)

            
            print("Seleccione una opción a modificar")
            print()
            print("[1] código de la herramienta")
            print("[2] tipo de herramienta")
            print("[3] disponibilidad de registro")
            print("[4] ubicación")
            print("[5] Unidades disponibles ")
            opcion = input()

            if(opcion == 1):
                print("Ingrese el nuevo código de la herramienta")
                nuevo_codHerramienta = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Herramientas SET codHerramienta WHERE codHerramienta = nuevo_codHerramienta;"
			            cursor.execute(consulta, (2000))

                        datos_Herramienta = cursor.fetchall()

                        for Herramientas in datos_Herramienta:
				                    print(Herramientas)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 2):
                print("Ingrese el nuevo tipo de herramienta")
                nuevo_tipoHerramienta = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Herramientas SET tipoHerramienta WHERE tipoHerramienta = nuevo_tipoHerramienta;"
			            cursor.execute(consulta, (2000))

                        datos_Herramienta = cursor.fetchall()

                        for Herramientas in datos_Herramienta:
				                    print(Herramientas)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)


            if(opcion == 3):
                print("Ingrese nueva disponibilidad")
                nueva_Disponibilidad = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Herramientas SET disponibilidad WHERE disponibilidad = nueva_Disponibilidad;"
			            cursor.execute(consulta, (2000))

                        datos_Herramienta = cursor.fetchall()

                        for  Herramientas in datos_Herramienta:
				                    print(Herramientas)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 4):
                print("Ingrese nueva ubicación")
                nueva_Ubicacion = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Herramientas SET ubicacion WHERE ubicacion = nueva_Ubicacion;"
			            cursor.execute(consulta, (2000))

                        datos_Herramienta = cursor.fetchall()

                        for  Herramientas in datos_Herramienta:
				                    print(Herramientas)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 5):
                print("Ingrese nuevas unidades disponibles")
                nuevas_UnidadesDisponibles = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Herramientas SET unidadesDisponibles WHERE unidadesDisponibles  = nuevas_UnidadesDisponibles;"
			            cursor.execute(consulta, (2000))

                        datos_Herramienta = cursor.fetchall()

                        for  Herramientas in datos_Herramienta:
				                    print(Herramientas)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)


            
	finally:
		conexion.close()
	
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)




def Modificar_Insumos():

    print("Ingrese el código del insumo")
    codigo_Insumo = input()

     try:
	    conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	    try:
		with conexion.cursor() as cursor:
			
			consulta = "SELECT codInsumos, tipoInsumos, disponibilidad, unidadesDisponibles, ubicacion FROM Insumos WHERE codInsumos = codigo_Insumo;"
			cursor.execute(consulta, (2000))

			datos_Insumo = cursor.fetchall()

		
			for Insumos in datos_Insumo:
				print(Insumos)


            print("Seleccione una opción a modificar")
            print()
            print("[1] código del insumo")
            print("[2] Tipo de insumo")
            print("[3] Disponibilidad")
            print("[4] Unidades disponibles")
            print("[5] Ubicación ")
            opcion = input()

            if(opcion == 1):
                print("Ingrese el nuevo código del insumo")
                nuevo_codInsumos = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Herramientas SET codInsumos WHERE codInsumos = nuevo_codInsumos;"
			            cursor.execute(consulta, (2000))

                        datos_Insumo = cursor.fetchall()

                        for Insumos in datos_Insumo:
				                    print(Insumos)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 2):
                print("Ingrese el nuevo tipo de insumo")
                nuevo_tipoInsumo = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Insumos SET tipoInsumos WHERE tipoInsumos = nuevo_tipoInsumo;"
			            cursor.execute(consulta, (2000))

                        datos_Insumo = cursor.fetchall()

                        for Insumos in datos_Insumo:
				                    print(Insumos)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)


            if(opcion == 3):
                print("Ingrese nueva disponibilidad")
                nueva_Disponibilidad = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Insumos SET disponibilidad WHERE disponibilidad = nueva_Disponibilidad;"
			            cursor.execute(consulta, (2000))

                        datos_Insumo = cursor.fetchall()

                        for  Insumos in datos_Insumo:
				                    print(Herramientas)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 4):
                print("Ingrese nuevas unidades disponibles")
                nuevas_UnidadesDisponibles = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Insumos SET unidadesDisponibles WHERE unidadesDisponibles = nuevas_UnidadesDisponibles;"
			            cursor.execute(consulta, (2000))

                        datos_Insumo = cursor.fetchall()

                        for  Insumos in datos_Insumo:
				                    print(Insumos)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 5):
                print("Ingrese la nueva ubicación")
                nueva_Ubicación = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE Insumos SET ubicacion WHERE ubicacion  = nueva_Ubicacion;"
			            cursor.execute(consulta, (2000))

                        datos_Insumo = cursor.fetchall()

                        for  Insumos in datos_Insumo:
				                    print(Insumos)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)

            
	finally:
		conexion.close()
	
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)



def Modificar_EPP():

    print("Ingrese el código del EPP")
    codigo_EPP = input()

     try:
	    conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	    try:
		  with conexion.cursor() as cursor:
			
			consulta = "SELECT codEPP, tipoEPP, disponibilidad, unidadesDisponibles, ubicacion FROM EPP WHERE codEPP = codigo_EPP;"
			cursor.execute(consulta, (2000))

			datos_EPP = cursor.fetchall()

		
			for EPP in datos_EPP:
				print(EPP)


            print("Seleccione una opción a modificar")
            print()
            print("[1] Código del EPP")
            print("[2] Tipo de EPP")
            print("[3] Disponibilidad ")
            print("[4] Unidades disponibles")
            print("[5] Ubicación")
            opcion = input()

            if(opcion == 1):
                print("Ingrese el nuevo código del EPP")
                nuevo_codEPP = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE EPP SET codEPP WHERE codEPP = nuevo_codEPP;"
			            cursor.execute(consulta, (2000))

                        datos_EPP = cursor.fetchall()

                        for EPP in datos_EPP:
				                    print(EPP)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 2):
                print("Ingrese el nuevo tipo de EPP")
                nuevo_tipoEPP = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE EPP SET tipoEPP WHERE tipoEPP = nuevo_tipoEPP;"
			            cursor.execute(consulta, (2000))

                        datos_EPP = cursor.fetchall()

                        for EPP in datos_EPP:
				                    print(EPP)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)


            if(opcion == 3):
                print("Ingrese nueva disponibilidad")
                nueva_Disponibilidad = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE EPP SET disponibilidad WHERE disponibilidad = nueva_Disponibilidad;"
			            cursor.execute(consulta, (2000))

                        datos_EPP = cursor.fetchall()

                        for EPP in datos_EPP:
				                    print(EPP)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 4):
                print("Ingrese la nuevas unidades disponibles")
                nuevas_UnidadesDisponibles = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE EPP SET unidadesDisponibles WHERE unidadesDisponibles = nuevas_UnidadesDisponibles;"
			            cursor.execute(consulta, (2000))

                        datos_EPP = cursor.fetchall()

                        for  EPP in datos_EPP:
				                    print(EPP)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)



            if(opcion == 5):
                print("Ingrese la nueva ubciacion")
                nueva_Ubicacion = input()

                try:
	                conexion = pymysql.connect(host='3306',
                             user='root',
                             password='',
                             db='mydb')
	                try:
		                with conexion.cursor() as cursor:
			            consulta = "UPDATE EPP SET ubicacion WHERE ubicacion  = nueva_Ubicacion;"
			            cursor.execute(consulta, (2000))

                        datos_EPP = cursor.fetchall()

                        for  EPP in datos_EPP:
				                    print(EPP)

                        print("Modificación Exitosa")

                    finally:
                        conexion.close()

                    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:

	                     print("No se puede realizar la modificación: ", e)

            
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
