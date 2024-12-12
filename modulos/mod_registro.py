from modulos.mod_base import interc as I
from datetime import datetime

#inicializar
bd = I()

#funcion para registrar gasto
def reg_gasto():
    print("REGISTRO DE GASTO")
    print("____________________")
    fecha = input("Ingrese la fecha del gasto (dd/mm/aaaa): ")
    descripcion = input("Ingrese la descripcion del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    persona = input("Ingrese la persona quien realizo el pago")
    fecha_registro = datetime.now().strftime("%d/%m/%Y")
    #aqui va la otra funcion (fecha,descripcion,monto,persona,fecha_registro)

def facturas_notaria():
    print("Registro de facturas de notaria")
    folio_fac = input("Ingrese el folio de la factura: ")
    concepto = input("Concepto: ")
    concepto_not = input("Concepto de Notaria: ")
    cantidad = int(input("Cantidad de certificaciones: "))
    fecha_sol = input("Ingrese la fecha de la solicitud (dd/mm/aaaa): ")
    monto = float(input("Monto "))
    solicitado = input("¿Quien solicito?")
    bd.reg_facturas_notaria((folio_fac,concepto,concepto_not,cantidad,fecha_sol,monto,solicitado))
    
    
print("Que desea registrar")
print("1.Certificaciones 2. Facturas 3. Gastos 4. Pagos")
op = int(input("Ingrese la opcion"))
if op == 1:
    pass
elif op == 2:
    facturas_notaria()
elif op == 3:
    pass
elif op == 4:
    pass