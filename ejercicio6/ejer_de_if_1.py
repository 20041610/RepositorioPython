"""Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo."""
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))

if numero1 > numero2:
    suma = numero1 + numero2
    resta = numero1 - numero2
    print("Su suma es: ", suma, "y su resta es: ", resta)
else:
    producto = numero1 * numero2
    division = numero1 / numero2
    print("Su producto es: ", producto, "y su division es: ", division)
