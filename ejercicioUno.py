ciclistas = {}
contador = 1
option = 0

while option != 1:
    print("---- MENU PROGRAMA CICLISTAS ----")
    print("1. Ingrese nuevo ciclista")
    print("2. Ver lista de ciclistas")
    print("3. Cambiar tiempo de un ciclista")
    print("4. Eliminar ciclista por codigo")
    print("5. Salir del programa")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        nombre = input("Digite el nombre: ")
        edad = input("Digite la edad: ")
        pais = input("Digite el país: ")
        equipo = input("Digite el equipo: ")
        tiempo = input("Digite el tiempo (en minutos): ")

        ciclista = {"Nombre": nombre, "Edad": edad, "País": pais, "Equipo": equipo, "Tiempo": tiempo}

        ciclistas[contador] = ciclista
        print("El código del ciclista es:", contador)
        contador += 1

    elif opcion == "2":
        print("*************** LISTA DE CICLISTAS *******************")
        for codigo, ciclista in sorted(ciclistas.items(), key=lambda x: x[1]["Tiempo"]):
            print("Código:", codigo)
            print("Nombre:", ciclista["Nombre"])
            print("Edad:", ciclista["Edad"])
            print("País:", ciclista["País"])
            print("Equipo:", ciclista["Equipo"])
            print("Tiempo:", ciclista["Tiempo"])
            print()

    elif opcion == "3":
        codigo = int(input("Digite el código del ciclista a corregir el tiempo: "))
        if codigo in ciclistas:
            tiempo = input("Digite el nuevo tiempo (en minutos): ")
            ciclistas[codigo]["Tiempo"] = tiempo
            print("Tiempo actualizado correctamente.")
        else:
            print("El código ingresado no existe.")

    elif opcion == "4":
        codigo = int(input("Digite el código del ciclista a eliminar: "))
        if codigo in ciclistas:
            del ciclistas[codigo]
            print("El ciclista se ha eliminado correctamente.")
        else:
            print("El código ingresado no existe.")

    elif opcion == "5":
        print("Fin del programa")
        break

    else:
        print("Opción incorrecta. Intente de nuevo.")
