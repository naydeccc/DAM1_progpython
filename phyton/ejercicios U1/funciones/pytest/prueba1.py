def mayor_que (numero1, numero2):
    x = numero1
    y = numero2
    if x < y:
        return y
    elif x > y:
        return x
    elif x == y:
        return 0
n1 = int(input("dame un numero: "))
n2 = int(input("dame un numero: "))
print(mayor_que(n1,n2))