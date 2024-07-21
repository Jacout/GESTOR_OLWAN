with open("datos.txt","r") as f:
    lineas = f.read().split(",") #las devuelve como lista

correo = lineas[0]
con = lineas[1]

print(correo)
print(con)