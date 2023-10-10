#inicio
#imprimir "dime tu nombre"
#lee nombre
#si nombre es igual a vacio entonces
#   nombre vale desconocido
#imprimir "dame la edad entre 0 y 125 años"
#lee edad
#mientras 125 < edad o edad < 1 entonces
#    imprime "dime la edad entre 0 y 125 años: "
#    lee edad
# n = 125 - edad
#imprimir "te llamas" + nombre + "y tienes {edad} años, te quedan aun" + n + "años por cumplir "
#fin
nombre = input("dime el nombre: ")
if nombre == "":
    nombre = " desconocido"
edad = int(input("dime la edad entre 0 y 125 años: "))
while 125 < edad or edad < 1:
    edad = int(input("dime la edad entre 0 y 125 años: "))
n = 125 - int(edad)
print(f"te llamas {nombre} y tienes {edad} años, te quedan aun {n} años por cumplir ")