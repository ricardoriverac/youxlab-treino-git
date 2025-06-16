lista = []
cont = 0
maior = 0
while True:
    numeros = int(input('Digite um valor: '))
    if numeros == 999:
        break
    cont += 1
    lista.append(numeros)
    if numeros > maior:
        maior = numeros
lista.sort(reverse=True)
if 5 in lista:
    print('O número 5 esta na lista')
else:
    print('Não tem o número 5')
print(lista)
print(maior)
print(f'Foram digitados: {cont} números')
print


