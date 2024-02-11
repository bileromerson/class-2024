import math

numero = int(input("coloque um numero:"))

if numero% 3 == 0 and numero% 5 == 0:
    print("divisivel por 3 e 5")

elif numero% 3 == 0:
    print("divisivel por 3")

elif numero% 5 == 0:
    print("divisivel por 5")

else: 
    print("não e divisivel por 3 ou 5")