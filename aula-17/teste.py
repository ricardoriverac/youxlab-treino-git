# LISTAS


# Listas são mutáveis
# variavel = append 'x' adiciona algo a lista
# variavel = insert (0,'x') adiciona em tal posiçao
# del variavel[3] deleta o que está na posição 3
# -> lanche.pop(3)
# -> lanche.remove('elemento')
# lanche.pop() remove o ultimo elemento
# valores = list(range(4,11))  4 5 6 7 8 9 10
# valores = [8,2,5,4,3,9,0]    valores.sort() 0 2 3 4 5 8 9
# valores.sort(reverse=True) 9 8 5 4 3 2 0 

# num = [4, 9, 2, 0, 1]
# num[2] = 3
# num.append(7)
# num.insert(6,8)
# num.sort()
# if 8 in num:
#     num.remove(8)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(1)

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v} ')
# print('FIM DA LISTA')



# valores = list()
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}.')

# valores.sort()
# print(valores)

# a = [2, 3, 4, 7]
# b = a[:]
# b[2] =8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')