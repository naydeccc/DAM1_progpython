#Desarrolla una función en prueba1.py que reciba dos números y retorne el mayor número de los dos o 0 si son iguales. 
#Realiza las pruebas unitarias y ejecútalas con pytest desde la terminal (puedes hacerlo en la terminal dentro de Visual Studio Code).
#
#Entrega lo siguiente:
#
#Los ficheros prueba1.py y test_prueba1.py
#Un pantallazo donde se muestre la vista del Explorador (View -> Explorer) con las carpetas y ficheros del proyecto.
#Un pantallazo del terminal con las pruebas unitarias detalladas realizadas con éxito.
#Fuerza un error en tu código, no en los tests, y muestra un pantallazo de tus pruebas unitarias realizadas de nuevo.
def mayor(n1,n2):
    if n1 == n2:
        return "el numero mayor es 0"
    elif n1 > n2:
        return "el numero mayor es " + str(n1)
    elif n2 > n1:
        return "el numero mayor es " + str(n2)

numero =3
numero2 = 3
print(mayor(numero,numero2))