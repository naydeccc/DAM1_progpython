#inicio
#lee numero1
# lee numero2
# si ( numero1 > numero2 ) entonces
#   n = numero2 - numero1
#   imprimir "el numero menor es" + numero 2 + "y entre ellos existe" + n  + "numero "
# si ( numero1 < numero2 ) entonces
#   n = numero2 - numero1
#   imprimir "el numero menor es" + numero 1 + "y entre ellos existe" + n  + "numero "
# si ( numero1 == numero2 ) entonces
#   imprimir "Los numeros no pueden ser iguales"
#fin
numero_1 = int(input("dame un numero: "))
numero_2 = int(input("dame otro un numero: "))
if numero_1 > numero_2:
    n = numero_1-numero_2
    print(f"el numero menor es {numero_2} y entre ellos existen {n}  numeros")
elif numero_1 < numero_2:
    n = numero_2-numero_1
    print(f"el numero menor es {numero_1} y entre ellos existen {n}  numeros")
elif numero_1 == numero_2:
    print("Los numeros no pueden ser iguales")