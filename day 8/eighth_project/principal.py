import numeros as num  


def menu():
    while True:
        print("""
        [1] - Perfumería
        [2] - Farmacia
        [3] - Cosméticos
        """)
        eleccion = input("Ingresa una opción: ")

        if eleccion.isdigit() and int(eleccion) in range(1, 4):
            return int(eleccion)
        else:
            print("❌ Opción inválida. Intenta nuevamente.\n")


def menu_salir():
    while True:
        print("""
        [1] - Pedir otro turno
        [2] - Salir
        """)
        eleccion = input("Ingresa una opción: ")

        if eleccion.isdigit() and int(eleccion) in range(1, 3):
            return int(eleccion)
        else:
            print("❌ Opción inválida. Intenta nuevamente.\n")


def terminar():
    return menu_salir() == 2 


def iniciar():
    terminar_programa = False

    # Instancias de los turnos decoradosﬁ
    turno_perfumeria = num.decorador(num.generador_perfumeria)
    turno_farmacia = num.decorador(num.generador_farmacia)
    turno_cosmeticos = num.decorador(num.generador_cosmeticos)

    while not terminar_programa:
        eleccion = menu()

        if eleccion == 1:
            turno_perfumeria()
        elif eleccion == 2:
            turno_farmacia()
        elif eleccion == 3:
            turno_cosmeticos()

        terminar_programa = terminar()

    print("\n👋 Gracias por usar el sistema de turnos.")