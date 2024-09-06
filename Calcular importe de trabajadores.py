sueldobásico= float(input("ingresar sueldo básico: "))
antigüedad= int(input("ingresar antigüedad: "))
estadocivil=int(input("Ingresar estado civil (1 para soltero y 2 para casado): "))

# antiguedad
if estadocivil == 1:
    montoAntiguedad = (antigüedad*sueldobásico*5)/100
else:
    montoAntiguedad = (antigüedad*sueldobásico*7)/100

jubilación= sueldobásico*11/100
obrasocial= sueldobásico*3/100
sindicato=sueldobásico*3/100
descuentos= jubilación+obrasocial+sindicato
print ("estado civil: ", estadocivil, "sueldo básico: $", sueldobásico, "antigüedad: ", antigüedad, "años", "descuentos: ",
       "jubilación: ", jubilación, "obrasocial: ", obrasocial, "sindicato: ", sindicato,"total de descuentos:", descuentos)
if estadocivil == 1:
    print ("importe: $", (montoAntiguedad+sueldobásico)-descuentos)
elif estadocivil == 2:
    print("importe: $", (montoAntiguedad+sueldobásico)-descuentos)