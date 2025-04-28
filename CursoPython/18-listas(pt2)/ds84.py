temp=[]
princ=[]
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior=menor=temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=str(input('Quer continuar ? [S/N] '))
    if resp in 'Nn':
        break
print('==' * 20)
print(f'Ao todo o números de pessoas cadastradas foi {len(princ)}')
print(f'O maior peso foi {maior}')
for p in princ:
    if p[1]==maior:
        print(f'[{p[0]}]')
print()
print(str(f'O menor peso foi {menor}'))
for p in princ:
    if p[1]==menor:
        print(f'[{p[0]}]')
print()