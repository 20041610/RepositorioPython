"""Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"."""
nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2: "))
nota3 = int(input("Ingrese nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 7:
    print("Alumno Promocionado")
else:
    print("Alumno no promocionado")
     
