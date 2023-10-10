pan= 3.49
pandiapasado= 3.49 * 0.6
panvendido= int(input("Barras de pan vendidas: "))
barravendida= pandiapasado * panvendido
print(f"Una barra de pan cuesta {pan}€, pero se descuenta un 60% al no ser del dia.")
print(f"El coste final de todas las barras no del dia es: {round(barravendida, 2)}€.")