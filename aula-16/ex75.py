n = (int(input('Digite um número entre 0 e 10: ')),
     int(input('Mais um número: ')),
     int(input('Mais um: ')),
     int(input('Por fim, o último: ')))
print(f'Você digitou os valores {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:    
    print(f'O número 3 apareceu pela primeira vez na {n.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram: ',end = '')
for p in n:
    if p % 2 == 0:
        print(p, end=' ')




# valor = ()

# for a in range(4):
#     n = int(input('Digite um valor de 0 a 10: '))
#     valor += (n,)

# print(f'O número 9 apareceu {valor.count(9)} vezes')
# print(f'O número 3 apareceu pela primeira vez na {valor.index(3) + 1}ª posição')
# print(f'Os números pares digitados foram: ',end= '')

# for c in n:
#     if n % 2 == 0:
#         print(c,end='')