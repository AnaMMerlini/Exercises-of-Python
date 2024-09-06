salario = 0
legajo = 0
legajomayor = 0
empleados = 0
empleado200mil = 0
empleado50mil = 0
salario1 = 0
salario2 = 0
salario3 = 0
totalsalario = 0
menorganancia = salario
mayorganancia = salario
legajo = int (input("Ingresar el legajo de un empleado o -1 para finalizar: "))
while legajo != -1:
    categoría = int (input("Ingresar la categoría (1/2/3): "))
    salario = float (input("Ingresar un salario: "))
    totalsalario = totalsalario + salario
    if salario > mayorganancia:
        mayorganancia = salario
        legajomayor = legajo
    if salario < 50000:
        menorganancia = salario
    if salario > 200000:
        empleado200mil = empleado200mil + 1
    if categoría == 3 and salario < 50000:
        empleado50mil = empleado50mil + 1
    if categoría == 1:
        salario1 = salario1 + salario
    if categoría == 2:
        salario2 = salario2 + salario
    if categoría == 3:
        salario3 = salario3 + salario
    empleados = empleados + 1
    legajo = int (input("Ingresar el legajo de un empleado o -1 para finalizar: "))
promedio = totalsalario / empleados
print ("Importe total de salarios: ", totalsalario, "Cantidad de empleados que ganan más de $200000: ", empleado200mil, "Cantidad de empleados que ganan menos de 50000 de la categoría 3: ", empleado50mil, "Legajo del empleado que más gana", legajomayor, "Sueldomásbajo: ", menorganancia, "Importe total de ganancia de la categoría 1: ", salario1, "Importe total de ganancia de la categoría 2: ", salario2, "Importe total de ganancia de la categoría 3: ", salario3, "Salario promedio: ", promedio)