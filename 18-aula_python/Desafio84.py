temp = []
printc = []
mai = man = 0
while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if len (printc) == 0:
        mai = man = temp[1]
    else:
        if temp[1] >mai:
            mai = temp[1]
        if temp[1] < man:
            man = temp[1]
    printc.append(temp[:])
    temp.clear()
    responda = str(input('Deseja continuar? [S/N] '))
    if responda in 'Nn':
        break
print('=-'*30)
print(f'Você cadastrou {len(printc)} Pessoas!! ')
print(f'O maior peso cadastrado foi {mai}Kg. peso de ', end='' )
for p in printc:
    if p [1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {man}Kg. peso de ', end='')
for p in printc:
    if p[1] == man:
        print(f'[{p[0]}]', end='')
print()

