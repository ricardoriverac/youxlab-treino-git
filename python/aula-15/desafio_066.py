soma = cont = 0
while True:
    num = input('digite um valor ou [ X ] pra para: ')
    if num in str('Xx'):
        break
    else:
        cont += 1
        soma += int(num)
print(f'Você digitou {cont} números e a soma entre os valores é {soma}')