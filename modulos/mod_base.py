import sqlite3
import datetime

#clase para realizar tareas de base de datos
class interc():
    def __init__(self): #inicializa la conexion
        try:
            self.conn = sqlite3.connect('data/OLWAN_SERVICES.db')
        except sqlite3.Error as e:
            print("Error")
            with open(f"log_{datetime.now().strftime("%d/%m/%Y")}.txt","w") as f:
                f.write(str(e))
        
    #consultar el nombre de las tablas con sqlimaster
    def consulta_tablas(self):
        self.__init__()
        self.cursor = self.conn.cursor()
        tablas = list()
        for a in self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';"):
            if 'sqlite' in a[0]:
                continue
            else:
                tablas.append(a[0])
        self.conn.close()
        return tablas
    
    #registro de facturas notaria si guarda
    def reg_facturas_notaria(self,datos:tuple):
        self.__init__()
        self.cursor = self.conn.cursor()
        sentencia = """insert into certificaciones_pagos (folio_factura,concepto,concepto_notaria,cantidad,fecha_solicitado,monto,solicitado) 
        values(?,?,?,?,date(?),?,?);
        """
        if sqlite3.complete_statement(sentencia) == True:
            self.cursor.execute(sentencia,datos)
            self.conn.commit()
            print("Se guardo la informacion correctamente")
        self.conn.close()
        
    def registro_gastos(self,datos:tuple):
        self.__init__()
        self.cursor = self.conn.cursor()
        sentencia = "insert into gastos (concepto,monto,fecha,fecha_registro,realiza) values(?,?,date(?),date(?),?);"
        if sqlite3.complete_statement(sentencia) == True:
            self.cursor.execute(sentencia,datos)
            self.conn.commit()
            print("Gasto registrado con exito")
        self.conn.close()
    
    def registro_certificaciones(self,datos:tuple):
        self.__init__()
        self.cursor = self.conn.cursor()
        sentencia = """insert into certificaciones_2025 (identificacion,can_certi,costo,fe_solicitado,mes,cliente)
                    values(?,?,?,?,?,?);"""
        if sqlite3.complete_statement(sentencia) == True:
            self.cursor.execute(sentencia,datos)
            self.conn.commit()
            print("Se guardo la informacion correctamente")
        self.conn.close()

    def tabla(self,tabla):
        self.__init__()
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM {tabla}")
        return self.cursor.fetchall()
        

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