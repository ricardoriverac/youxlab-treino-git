num = int(input('Quanto você quer sacar?'))
total = num
ced = 50
totalCedula = 0
while True:
    if total >= ced:
        total -= ced
        totalCedula += 1
    else:
        print(f'Total de cédulas é de {totalCedula} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCedula = 0
        if total == 0:
            break