nrocliente = int (input("Ingrese el número del cliente: "))
totalfactura = float (input("Ingrese el total de la factura: "))
descuento2 = totalfactura * 2 / 100
cargo= totalfactura * 10 / 100
print ("Número de cliente: ", nrocliente, "Total de la factura: ", totalfactura)
if descuento2 < 200:
    unoaldiez = totalfactura - 200
    print ("Del 1 al 10, paga: $", unoaldiez)
else:
    unoaldiez = totalfactura - descuento2
    print ("Del 1 al 10, paga: $", unoaldiez)
print ("Del 11 al 20, paga: $", totalfactura)
if cargo > 350:
    mas20 = totalfactura + cargo
    print ("Pasado el 20, paga: $", mas20)
else:
    mas20 = totalfactura + 350
    print ("Pasado el 20, paga: $", mas20)