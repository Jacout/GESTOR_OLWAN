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
        
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            #llama al modulo para registro
            registro.menu()
        elif opcion == 2:
            #Llama al modulo para ver
            break
        elif opcion == 3:
            #Llama al modulo para exportar
            break
        elif opcion == 4:
            #Llama al modulo para editar/borrar
            break
        elif opcion == 5:
            #Llama al modulo para editar/borrar
            break
        else:
            print("Opción no válida, intente de nuevo")