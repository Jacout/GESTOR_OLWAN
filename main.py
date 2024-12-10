import modulos.mod_registro as registro

if __name__ == "__main__":
    while True:
        print("Registro OLWAN S.C.")
        print("Bienvenido")
        #menu para registrar un gasto o una tarea o salir
        print("1. Registro")
        print("2. Ver")
        print("3. Exportar")
        print("4. Editar/Borrar")
        
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            #llama al modulo para registrar gasto
            registro.reg_gasto()
        elif opcion == 2:
            #Llama al modulo de registro con la funcion de tarea
            registro.reg_tarea()
        elif opcion == 3:
            break
        elif opcion == 4:
            break
        else:
            print("Opción no válida, intente de nuevo")