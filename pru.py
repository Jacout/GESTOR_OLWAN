import sqlite3


fecha_sol = input("Ingrese la fecha que se solicito formato YYYY-MM-DD\n")
#obtener de la fecha sol el mes
mes_sol = int(fecha_sol[5:7])
print(mes_sol)