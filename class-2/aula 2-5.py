import math
'''
type a number and the code shows if
it is divisible by 3, 5, 3 and 5, or
neither of the two
'''
numero = int(input("coloque um numero:"))

if numero% 3 == 0 and numero% 5 == 0:
    print("divisivel por 3 e 5 \n(divisible by 3 and 5)")

elif numero% 3 == 0:
    print("divisivel por 3 \n(divisible by 3)")

elif numero% 5 == 0:
    print("divisivel por 5 \n(divisible by 5)")

else: 
    print("não e divisivel por 3 ou 5 \n(neither of the two)")