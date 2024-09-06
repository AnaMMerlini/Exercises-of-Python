legajo = 0
aprobados = 0
desaprobados = 0
aplazados = 0
contador = 0
legajo = int (input("Ingrese número de legajo: "))
while legajo != -1:
    nota = float (input ("Ingrese nota de examen final: "))
    if nota > 10 or nota < 1:
        print ("Nota no válida")
    if nota <= 10 or nota >=1:
        if nota >= 4:
            aprobados = aprobados + 1
        elif nota < 4:
            desaprobados = desaprobados + 1
    if nota == 1:
        aplazados = aplazados + 1
    contador = contador + 1
    legajo = int (input("Ingrese número de legajo o -1 para finalizar: "))
porcentaje = (aplazados * 100) / contador
print ("Aprobados: ", aprobados, "Desaprobados: ", desaprobados, "Porcentaje de aplazados", porcentaje)