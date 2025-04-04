pessoas = list() 
dado = list()
maior = menor = 0
contarp = 0
while True:
    dado.append(str(input('Nome: '))) 
    dado.append(float(input('Peso: ')))
    contarp += 1
    sair = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if sair == 'N':
       break
    if  len(pessoas) == 0:
        menor = maior = dado[1]
    else:
        if dado[1] > maior :
            maior = dado[1]
        if dado[1] < menor :
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()

print(f'Ao todo , você cadastrou {contarp} pessoas')
print(f'O maior peso foi de {maior} , ', end='')
for p in pessoas:
    if p[1] == maior :
        print(f'[{p[0]}] ')
print(f'O menor peso foi de {menor}Kg', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]')

    