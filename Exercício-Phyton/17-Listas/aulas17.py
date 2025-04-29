#Listas usam []

#As listas são mutaveis, então se eu quiser colocar outra coisa dentro dela eu posso
#lanche = ['Hamburguer', 'Pizza', 'Suco', 'Pudim']
#lanche[3] = 'Sorvete'

#Comando que adiciona mais alguam coisa dentro de uma lista:
#lanche.append('Cookie')

#Comando que me faz adicionar alguma coisa em qualquer opção que eu quiser dentro de uma lista:
#lanche.insert(0,'Cachorrro Quente')

#Comandos que me fazem apagar alguma coisa dentro de uma lista:
#del lanche[2]

#O pop é usado mais para apagar o ultimo valor de uma lista, mas serve para outros também
#lanche.pop(3)

#Remove tem que colocar o conteudo do que voce quer tirar da lista
#lanche.remove('Pizza')

#SE tiver o conteudo 'Pizza' ele será removido
#if 'Pizza' in lanche:
#    lanche.remove('Pizza')

#Criar listas através de range:
#valores = list(range(4,11))

#Organizar a lista de menor pra maior
#valores = [8, 2, 5, 4, 9, 3, 0]
#valores.sort()

#Organizar a lista de forma inversa 
#valores.sort(reverse=True)
#len mostra quantos elementos tem dentro de uma lista
#len(valores)
#print(valores)

#---------------------------------------------

# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 5')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

#Outra forma de fazer   
#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista')

#Outra forma de fazer
#valores = list()
#for cont in range (0, 5):
#    valores.append(int(input('Digite um valor:')))

#for c, v in enumerate(valores):
#    print(f'Na posução {c} encontrei o valor {v}!')
#print('Chegei ao final da lista.')

#Outro exemplo
#a = [2, 3, 4, 7]
#b = a[:]
#b[2] = 8    
#print(f'Lista A: {a}')
#print(f'Lista B: {b}')