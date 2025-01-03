from modulos.mod_base import interc as I
from datetime import datetime

#inicializar
bd = I()

#funcion para registrar gasto
def reg_gasto():
    print("REGISTRO DE GASTO")
    print("____________________")
    fecha = input("Ingrese la fecha del gasto (aaaa-mm-dd): ")
    concepto = input("Ingrese la descripcion del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    persona = input("Ingrese la persona quien realizo el pago: ")
    fecha_registro = datetime.now().strftime("%Y-%m-%d")
    datos_g = (concepto,monto,fecha,fecha_registro,persona)
    bd.registro_gastos(datos_g)

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

def certificaciones():
    print("Registro de Certificaciones")
    ident = input("Ingrese identificacion del documento, como nombre de archivo o numero economico\n")
    canti_cer = int(input("Cantidad de certificaciones\n"))
    hojas = int(input("Tiene hojas extra el documento? 1.Si 2.No \n"))
    costo = 225
    if hojas == 1:
        hojas_extra = int(input("¿Cuantas hojas tiene extra?"))
        costo = costo + (10 * hojas_extra)
    subtotal = costo * canti_cer
    
    fecha_sol = input("Ingrese la fecha que se solicito formato YYYY-MM-DD\n")
    #obtener de la fecha sol el mes
    mes_sol = int(fecha_sol[5:7])
    
    cliente = int(input("Ingrese el ID del cliente a quien se certifico"))
    bd.registro_certificaciones((ident,canti_cer,subtotal,fecha_sol,mes_sol,cliente))
        
    

def menu():    
    print("Que desea registrar")
    print("1.Certificaciones 2. Facturas 3. Gastos 4. Pagos")
    op = int(input("Ingrese la opcion"))
    if op == 1:
        certificaciones()
    elif op == 2:
        facturas_notaria()
    elif op == 3:
        reg_gasto()
    elif op == 4:
        pass