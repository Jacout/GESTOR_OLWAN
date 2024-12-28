import sqlite3
import datetime

#clase para realizar tareas de base de datos
class interc():
    def __init__(mismo): #inicializa la conexion
        try:
            mismo.conn = sqlite3.connect('OLWAN_SERVICES.db')
        except sqlite3.Error as e:
            print("Error")
            with open(f"log_{datetime.now().strftime("%d/%m/%Y")}.txt","w") as f:
                f.write(str(e))
        
    #consultar el nombre de las tablas con sqlimaster
    def consulta_tablas(mismo):
        mismo.__init__()
        mismo.cursor = mismo.conn.cursor()
        for a in mismo.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';"):
            print(a[0])
        tablas = mismo.cursor.fetchall()
        mismo.conn.close()
        return tablas
    
    #registro de facturas notaria si guarda
    def reg_facturas_notaria(mismo,datos:tuple):
        mismo.__init__()
        mismo.cursor = mismo.conn.cursor()
        sentencia = """insert into certificaciones_pagos (folio_factura,concepto,concepto_notaria,cantidad,fecha_solicitado,monto,solicitado) 
        values(?,?,?,?,date(?),?,?);
        """
        if sqlite3.complete_statement(sentencia) == True:
            mismo.cursor.execute(sentencia,datos)
            mismo.conn.commit()
            print("Se guardo la informacion correctamente")
        mismo.conn.close()
        
    def registro_gastos(mismo,datos:tuple):
        mismo.__init__()
        mismo.cursor = mismo.conn.cursor()
        sentencia = "insert into gastos (concepto,monto,fecha,fecha_registro,realiza) values(?,?,date(?),date(?),?);"
        if sqlite3.complete_statement(sentencia) == True:
            mismo.cursor.execute(sentencia,datos)
            mismo.conn.commit()
            print("Gasto registrado con exito")
        mismo.conn.close()
        
#incializar la clase
#cone = interc()


#cone.consulta_tablas()

'''
with open("archivo.txt","w") as f:
    for a in tablas:
        f.write(f"{str(a[0])} \n")

print(tablas)
print()
for a in tablas:
    print(f"Tabla {a}")
    '''