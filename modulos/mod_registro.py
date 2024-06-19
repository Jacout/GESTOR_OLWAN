import modulos.mod_bd as db
from datetime import datetime

#funcion para registrar gasto

def reg_gasto():
    print("REGISTRO DE GASTO")
    print("____________________")
    fecha = input("Ingrese la fecha del gasto (dd/mm/aaaa): ")
    descripcion = input("Ingrese la descripcion del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    persona = input("Ingrese la persona quien realizo el pago")
    fecha_registro = datetime.now().strftime("%d/%m/%Y")
    db.insertar_gasto(fecha,descripcion,monto,persona,fecha_registro)

def reg_tarea():
    print("REGISTRO DE TAREA")
    print("____________________")
    titulo = input("Ingrese el titulo de la tarea")
    descripcion = input("Ingrese la descripcion de la tarea")
    importancia = input("Nivel de importancia: Alta o Baja")
    fecha_registro = datetime.now().strftime("%d/%m/%Y")
    fecha_vencimiento = input("Ingrese la fecha del gasto (dd/mm/aaaa): ")
    db.insertar_tarea(titulo, descripcion, importancia, fecha_registro, fecha_vencimiento)