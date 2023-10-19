cond1 = 0
cond2 = 0
if cond1 == 0 :#si cond1 se cumple decuelve true
    print("funciona el if")
else:#si el if no se cumple, se hace el else
    print("funciona el else")
if cond1 == 0 :#si cond1 se cumple decuelve true
    print("funciona el if")
elif cond1 < 1 :# es como el if pero si se cumple uno, no se hace las demas lineas
    print("si se cumple esto no se ejecuta el elif de abajo")
elif cond1 < 1 :# es como el if pero si se cumple uno, no se hace las demas lineas
    print("este no se va a imprimir")
while cond1 < 1:# es un bucle infinito, hasta que al condicon no se cumpla
    print("se ejecutara infinita veces hasta que la condicion no se cumpla")
for cond in 1,9:# es un bucle finito, se repite las veces que quieras
    print("nose que hace")
(1<2)#1 menor que 2
(1>2)#1 mayor que 2
(1>=2)#1 mayor o igual que 2
(1<=2)#1 menor o igual que 2
(1!=2)#1 es distinto de 0
(1==2)# 1 es igual que 2
cond1 and cond2 #cond1 y cond2(devuelve true si se cumplen las dos)
cond1 or cond2#cond1 o cond2(devuelve true si se cumplen una de las dos)
cond1.replace