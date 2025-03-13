'''
var1 = float(input('digite o numero: '))
var2 = float(input('digite o segundo numero: '))

mais = var1 + var2
menos = var1 - var2
divisao = var2 / var1
multiplicacao = var1 * var2

print(f'sua soma deu: {mais}')
print(f'sua subtraçao deu: {menos}')
print(f'sua divisão deu: {divisao}')
print(f'sua multiplicação deu: {multiplicacao}')
'''
''''''
# (a == b) se os valores de dois operandos forem iguais, a condição torna-se verdadeira
# (a != b) se os valores de dois operandos forem diferentes, a condição torna-se verdadeira
# (a > b) se o valor do operando A for maior que o valor do operando B, a condição torna-se verdadeira
# (a < b) se o valor do operando A for menor que o valor do operando B, a condição torna-se verdadeira
# (a >= b) se o valor do operando A for maior ou igual que o valor do operando B, a condição torna-se verdadeira
# (a <= b) se o valor do operando A for menor ou igual que o valor do operando B, a condição torna-se verdadeira

nota = float(input('sua nota: '))
if nota <= 6:
    print('sucesso!')
else:
    print('tente novamente')