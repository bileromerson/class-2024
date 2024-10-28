
item = []
# adicionar
def adicionarAcrescimos(item):
    print('\n<--------------------- ADICIONAR --------------------->')
    print('O que gostaria de adicionar como acrescimo?')
    while '0' not in item:
        item.append(input('- '))
    else:
        item.remove('0')
        return item
# remover
def removerAcrescimos(item):
    print('\n<--------------------- REMOVER --------------------->')
    print('Gostaria de remover algo?')
    print(f'Pedido: {item}')
    while '0' not in item:
        removido = input('- ')
        if removido == '0':
            break
        elif removido not in item:
            print('Acréscimo não encontrado, escolha novamente: ')
            continue
        else: 
            item.remove(removido) 
    else:
        return item
# menu
print('\n<--------------------- AÇAÍ --------------------->')
menu = input('0) Finalizar pedido.\n1) Adicionar acréscimo.\n2) Remover acréscimo.\n\nO que gostaria de fazer? ')
while menu != '0':
    if menu == '1':
        adicionarAcrescimos(item)
        print('\n<--------------------- AÇAÍ --------------------->')
        print(f'Pedido: {item}')
        menu = input('0) Finalizar pedido.\n1) Adicionar acréscimo.\n2) Remover acréscimo.\n\nO que gostaria de fazer? ')
elif menu == '2':
        removerAcrescimos(item)
        print('\n<--------------------- AÇAÍ --------------------->')
        print(f'Pedido: {item}')
        menu = input('0) Finalizar pedido.\n1) Adicionar acréscimo.\n2) Remover acréscimo.\n\nO que gostaria de fazer? ')
    else: 
        menu = input('Comando inválido, digite novamente: ')
else:
    print(f'Pedido: {item}')