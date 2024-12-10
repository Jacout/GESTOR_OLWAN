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
        mismo.cursor = mismo.conn.cursor()
        mismo.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        tablas = mismo.cursor.fetchall()
        return tablas
    
cone = interc()


tablas = cone.consulta_tablas()


with open("archivo.txt","w") as f:
    for a in tablas:
        f.write(f"{str(a[0])} \n")

print(tablas)
print()
for a in tablas:
    print(f"Tabla {a}")