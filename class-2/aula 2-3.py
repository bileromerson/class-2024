
genero = input("digite 'H' sevocê for homem e 'M' se for mulher: \n ")
altura = float(input("digite sua altura: \n"))
if genero == "H" or genero == "h":
    print(round((72.7* altura)-58, 3))

elif genero == "M" or genero == "m":
    print(round((62.1* altura)-44.7, 3))

else:
    print("valor ivalido.")
