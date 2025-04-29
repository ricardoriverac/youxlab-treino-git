#GUANABARA
listanum = []
maior = 0
menor = 0 
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(F'Você digitou os valores: {listanum}')
print(F'O maior número digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(F'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()




#CODIGO ABAIXO FUNCIONA POREM SELECIONA APENAS UM NÚMERO MAIOR E UM MENOR
# valores = list()
# for numeros in range(0, 5):
#     valores.append(int(input(f'Digite um valor para a posição {numeros}: ')))


# maximo = max(valores)
# minimo = min(valores)



# print(F'Você digitou os valores: {valores}')
# print(F'O maior valor digitado foi {maximo} na posição : {valores.index(maximo)}')
# print(F'O menor valor digitado foi {minimo} na posição : {valores.index(minimo)}')