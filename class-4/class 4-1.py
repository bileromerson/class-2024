
nome = input("dijite um nome de usuario:  ")
senha = input("dijite uma senha:  ")
senhaInput = input("dijite sua senha: ")

while senhaInput != senha:
    senha = input("dijite uma senha novamente:  ")
    senhaInput = input("dijite novamente: ")

else:
    print("você criou o usuario")

nomeLogin = input("dijite seu nome de usuario: ")
senhaLogin = input("dijite sua senha:  ")
tentativas = 0

while senhaLogin != senha or nomeLogin != nome:
    tentativas += 1
    if tentativas > 3:
        print("sua conta foi bloqueada.")
        break
    else:
        senhaLogin = input("dijite seu nome de usuario novamente: \n")
        senha = input("dijite sua senha novamente:  ")