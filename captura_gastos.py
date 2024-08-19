import openpyxl

# Crear un objeto Workbook
wb = openpyxl.Workbook()

# Seleccionar la hoja de trabajo activa
sheet = wb.active

# Establecer el título de la hoja de trabajo
sheet.title = "Gastos"

# Establecer los títulos de las columnas
sheet['A1'] = "Fecha"
sheet['B1'] = "Descripción"
sheet['C1'] = "Monto"

# Función para capturar gastos
def capturar_gasto():
    fecha = input("Ingrese la fecha del gasto (dd/mm/yyyy): ")
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    return fecha, descripcion, monto

# Capturar gastos y guardarlos en la hoja de trabajo
while True:
    fecha, descripcion, monto = capturar_gasto()
    sheet.append([fecha, descripcion, monto])
    respuesta = input("¿Desea capturar otro gasto? (s/n): ")
    if respuesta == 'n':
        break

# Guardar el archivo Excel
wb.save("gastos.xlsx")

print("Gastos guardados con éxito en el archivo gastos.xlsx")