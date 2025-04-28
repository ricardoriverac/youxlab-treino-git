num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
# num.pop(2) 
# num.remove(2)
print(f'Essa lista tem {len(num)} elementos ')
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5 ')
print(num)

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

for v in valores:
    print(f'{v}...', end = '')
print('')

for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
    
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}! ')
print('Cheguei ao final da lista. ')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

