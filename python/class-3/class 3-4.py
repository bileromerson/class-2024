soma = 0
x = 0

while x<1000:
    x += 1 
    if x % 3 == 0:
        print(x)
        soma += x
    else:
        if x % 5 == 0:
            pass
        else:
            print('buscando...')
            continue
    if soma > 300:
        print(soma)
        break