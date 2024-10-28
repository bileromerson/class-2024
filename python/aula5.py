'''
ponto = 100
linhadechegagda = True
if linhadechegagda == true or ponto <= 100;
    print("parabens")

if linhadechegagda == true and ponto <= 100;
    print("parabens")
'''
numero = int(input("digite um numero de 1 a 12: "))
mes = ["janeiro","fevereiro","marso","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
if numero >=13 or numero < 1:
    print("deve ser usado somente numeros de 1 a 12 \ntente novamente")

else:
    print(mes[numero-1])