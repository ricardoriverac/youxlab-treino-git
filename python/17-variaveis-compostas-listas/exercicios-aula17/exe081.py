valores = []
cont = 0
while True:
    numero = int(input('Digite o valor:'))
    valores.append(numero)
    cont += 1
    sair = str(input('Quer continuar (S/N) ')).upper().strip()[0]
    if sair ==  'N' :
        break
print(f'Você digitou {cont} números')
print(f'Os valores em ordem decrescente{sorted(valores, key=int, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O 5 não faz parte da lista!')
