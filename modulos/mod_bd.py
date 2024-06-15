import sqlite3
import os


#crear la conexion en una funcion
def crear_conexion():
    conn = sqlite3.connect('olwan_data.db')
    return conn
#funcion para crear tablas principales
def crear_tablas():
    conn = crear_conexion()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS gastos
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              fecha TEXT,
              descripcion TEXT,
              monto REAL,
              persona TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS tareas
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              titulo TEXT,
              descripcion TEXT,
              importancia TEXT,
              fecha_registro TEXT,
              fecha_vencimiento TEXT)''')
    conn.commit()
    conn.close()

#funcion para insertar datos en la tabla gastos
def insertar_gasto(fecha, descripcion, monto, persona):
    conn = crear_conexion()
    c = conn.cursor()
    datos=[fecha,descripcion,monto,persona]
    c.execute("INSERT INTO gastos (fecha, descripcion, monto, persona) VALUES (?, ?, ?, ?)",datos)
    
    conn.commit()
    conn.close()
    

#funcion para insertar datos en la tabla de tareas
def insertar_tarea(titulo, descripcion, importancia, fecha_registro, fecha_vencimiento):
    conn = crear_conexion()
    c = conn.cursor()
    datos=[titulo,descripcion,importancia,fecha_registro,fecha_vencimiento]
    c.execute("INSERT INTO tareas (titulo, descripcion, importancia, fecha_registro, fecha_vencimiento) VALUES (?,?,?,?)",datos)


crear_tablas()
insertar_gasto('2022-01-01', 'comida', 100, 'Juan')
