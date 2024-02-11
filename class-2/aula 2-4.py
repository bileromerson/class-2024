import math
'''
type a number and if the number is negative
it shows the square and if it is positive
it shows the square root of the number
'''
numero = float(input("digite um numero:  "))
if numero <= -1:
    print(math.pow(numero, 2))
    print("negativo(negative)")
else:
    print(round(math.sqrt(numero), 4))
    print("positivo(positive)")
