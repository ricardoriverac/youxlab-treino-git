print('-'*30)
print('{:^30}'.format('BANCO YOUZ'))
print('-'*30)
valor = int(input('Qual valor você quer sacar R$'))
total = valor
cedulas = 50
totaldeCedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totaldeCedulas += 1
    else:
        if totaldeCedulas > 0:
            print(f'Total de {totaldeCedulas} cedulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20 :
            cedulas = 10
        elif cedulas == 10 :
            cedulas = 5
        elif cedulas == 5 :
            cedulas = 1
        totaldeCedulas = 0
        if total == 0:
            break
print('{:^30}'.format('\033[31m-----------------\033[m'))
print('O instituito \033[1;31mYOUX\033[m sempre a disposição')
print('{:^30}'.format('\033[31m-----------------\033[m'))