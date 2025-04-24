valores = []
maior = 0
menor = 0
# for cont in range(0,5):
#     numero = int(input(f'Digite o valor para a posição {cont}: '))
#     valores.append(numero)


#     if cont == 1 :
#         maior = menor = numero
#     else:
#         if numero > maior:
#             numero = maior
#         if numero < menor:
#             numero = menor

# print('-='*40)
# print(f'O maior valor digitado foi {maior} nas posições ', end='')
# for i , v in enumerate(valores):
#     if v == maior :
#         print(f'{i}...', end='')
# print()
# print(f'O menor valor digitado foi {menor} nas posições ' , end='')
# for i , v in enumerate(valores):
#     if v == menor :
#         print(f'{i}...', end='')
# print()

valores = []
maior = menor = 0

for count in range (0,5):
    numero = (int(input(f'Digite um valor para a posição {count}: ')))
    valores.append(numero)

    #Maior e menor
    if count == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print('-='*40)
print (f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end= '')
for i, v in enumerate(valores):
    if v == maior:
        print (f'{i} ... ', end= '')
print()
print (f'O menor valor digitado foi {menor} nas poisções ', end= '')
for i, v in enumerate(valores):
    if v == menor:
        print (f'{i} ... ', end= '')
print()