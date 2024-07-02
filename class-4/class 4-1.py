
nome = input("digite um nome de usuario:  ")
senha = input("digite uma senha:  ")
senhaInput = input("digite sua senha: ")

while senhaInput != senha:
    senha = input("digite uma senha novamente:  ")
    senhaInput = input("digite novamente: ")

else:
    print("você criou o usuario")

nomeLogin = input("digite seu nome de usuario: ")
senhaLogin = input("digite sua senha:  ")
tentativas = 0

while senhaLogin != senha or nomeLogin != nome:
    tentativas += 1
    if tentativas > 3:
        print("sua conta foi bloqueada.")
        break
    else:
        nomeLogin = input("digite seu nome de usuario novamente: \n")
        senhaLogin = input("digite sua senha novamente:  ")

else:
    print("você entrou na sua conta")
