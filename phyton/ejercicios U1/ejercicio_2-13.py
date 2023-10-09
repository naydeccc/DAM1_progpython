n = int(input("dame el primer numero:"))
m = int(input("dame el segundo numero:"))
c = n // m
r = n % m
print("la division de {:.2f} entre {:.2f} da un cociente {:.2f} y un resto {:.2f}".format(n, m, c, r))