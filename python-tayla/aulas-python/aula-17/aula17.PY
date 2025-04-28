#modificando uma lista
num = [2, 5, 9, 1]
num[2] = 3

# #adicionando um número
num.append(7)
num.insert(2,2)

# #colocando em ordem crescente e decrescente
num.sort()
num.sort(reverse=True)

# #removendo elementos
num.pop(2)
num.remove(2) #elimina so o primeiro caso tenha dois numeros =
print(num)

#mostrando os valores de uma forma bonitinha
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fim da lista')

#colocando valores em listas
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fim da lista')

#fazendo ligação de uma lista com outra
a = [2, 3, 4, 7]
b = a
b[2] = 8 #dps q iguala uma lista na outra cria uma ligação entre elas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#fazendo uma copia de lista
a = [2, 3, 4, 7]
b = a[:] #não cria uma ligação e sim copia tudo q ta na lista A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')