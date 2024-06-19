import openpyxl
import sqlite3
import mod_bd as bd
#realizar consulta de los datos de la tabla gastos e importarlos a excel con openpyxl
#conectar a la base de datos

def exportar(tabla):
    datos = bd.consulta_general(tabla)
    # Crear un libro de Excel
    wb = openpyxl.Workbook()
    #obtener la hoja activa
    ws = wb.active
    #asignar el título
    ws.title = "Gastos"

    #   asignar los títulos de las columnas
    ws['A1'] = 'ID'
    ws['B1'] = "Fecha"
    ws['C1'] = "Concepto"
    ws['D1'] = "Monto"
    ws['E1'] = "Persona"
    ws['F1'] = "Fecha registro"
    #insertar los datos
    for b in range(len(datos)):
        ws.append(datos[b])
    #darle tamaño a las celdas correspondiente
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 80
    ws.column_dimensions['D'].width = 10
    ws.column_dimensions['E'].width = 20
    ws.column_dimensions['F'].width = 15
    #guardar el archivo
    
    #apartado opcional solo aplica en gastos
    #se puede agregar formato a la celda
    total = 0
    for d in range(len(datos)):
        total += int(datos[d][3])
    #agregarlo despues del ultimo registro de la columna
    ws.cell(row=len(datos)+2, column=4).value = total
    
    wb.save("gastos.xlsx")


exportar("gastos")