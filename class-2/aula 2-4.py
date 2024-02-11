import math

numero = float(input("digite um numero:  "))
if numero <= -1:
    print(math.pow(numero, 2))
else:
    print(round(math.sqrt(numero), 4))
