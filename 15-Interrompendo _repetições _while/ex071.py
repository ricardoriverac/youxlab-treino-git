caixaE = int(input('Olá, qual valor você quer sacar? R$ '))

total = caixaE

cedula1 = 50
totced = 0
while True:
    if total >= cedula1:   
        total -= cedula1
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${cedula1}')
        if cedula1 == 50:
            cedula1 = 20
        elif cedula1 == 20:
            cedula1 = 10
        elif cedula1 == 10:
            cedula1 = 1
        totced = 0
        if total == 0:
            break