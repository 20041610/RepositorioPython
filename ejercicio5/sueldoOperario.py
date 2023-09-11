"""Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora."""
horas = int(input("Ingrese la cantidad de horas: "))
valor = int(input("Ingrese el valor por hora"))
sueldo = horas * valor
sueldo_mensual = sueldo * 4
print("El sueldo del mensual del operario es: ", sueldo_mensual)
