'''
nome = []
nome[1] = 'enzo' primeiro nome = enzo

nome.append('felipe') colocar na lista o nome felipe

nome.insert(1,'joao') colocar em primeiro lugar joao

print (nome)

del nome[1]deletar o primeiro nome

delet = nome.pop() deletar a ultima pessoa da lista

viajando= 'joao'
nome.remove(viajando) remover de nome as pessoas de viajando

print(f'{viajando} esta viajando')

nome.sort() colocar em ordem cresente
print (nome)
print (len(nome)) quantos itens tem na lista
'''
nome = []
nome.insert(0,input('nome:\n- '))
nome.insert(0,input('nome:\n- '))
nome.insert(0,input('nome:\n- '))
nome.insert(0,input('nome:\n- '))
nome.insert(0,input('nome:\n- '))
nome.insert(0,input('nome:\n- '))
nome.insert(0,input('nome:\n- '))
#o n/ serve para quebrar a linha
print(f'lista: {nome}')
