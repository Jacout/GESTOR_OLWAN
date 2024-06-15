import modulos.mod_registro

if __name__ == "__main__":
    while True:
        print("Registro OLWAN S.C.")
        print("Bienvenido")
        #menu para registrar un gasto o una tarea o salir
        print("1. Registrar Gasto")
        print("2. Registrar Tarea")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == 1:
            print("Llama al modulo de registro con la funcion de gasto")
        elif opcion == 2:
            print("Llama al modulo de registro con la funcion de tarea")
        elif opcion == 3:
            break
        else:
            print("Opción no válida, intente de nuevo")