
num = int(input("digite um numero de 1 a 10: \n"))
vezes = 0
while num > 10 or num < 0:
    print('o numero deve ser entre 1 e 10')
    num = int(input("digite um numero de 1 a 10: \n"))
else:
    for n in range(1, 11):
        vezes +=1
        print(f'{num} x {vezes} = {num * n}')
