print('-='*20)
print('{:^30}'.format('\033[1;35mCAIXA ELETRÔNICO\033[m'))
print('-='*20)
valor = int(input('Que valor você quer sacar? R$'))
ced = 200
totalCedula = 0
while True:
    if valor>=ced:
        valor-=ced
        totalCedula+=1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${ced}')
        if ced==200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        valor = 0
        if totalCedula == 0:
            break
