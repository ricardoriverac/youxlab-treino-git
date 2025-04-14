print('=' * 40)
nomeBanco = ('\033[1;35mBANCO DA CLARINHA\033[m')
print(f'{nomeBanco:^50}')
print('=' * 40)

#valor = int(input('Digite o valor que será sacado: R$'))
#MINHA FORMA DE CALCULAR
#cedula50 = valor//50
#valor = valor % 50
#cedula20 = valor//20
#valor = valor % 20  
#cedula10 = valor//10
#valor = valor % 10
#cedula5 = valor//5
#valor = valor % 5
#cedula1 = valor//1
#print('=' * 40)
#print(f'Notas de R$50: {cedula50}')
#print(f'Notas de R$20: {cedula20}')
#print(f'Notas de R$10: {cedula10}')
#print(f'Notas de R$5: {cedula5}')
#print(f'Notas de R$1: {cedula1}')
#print('=' * 40)

#COM O WHILE

valor = int(input('Digite o valor que será sacado: R$'))
cedula50 = cedula20 = cedula10 = cedula5 = cedula1 = 0
while valor >= 50:
    valor -= 50
    cedula50 += 1
while valor >= 20:
        valor -= 20
        cedula20 += 1
while valor >= 10:
        valor -= 10
        cedula10 += 1
while valor >= 5:
        valor -= 5
        cedula5 += 1
while valor >= 1:
        valor -= 1
        cedula1 += 1
enfeite = ('=' * 40)
print(f'\033[1;35m{enfeite}\033[m')
print(f'Notas de R$50: {cedula50}')
print(f'Notas de R$20: {cedula20}')
print(f'Notas de R$10: {cedula10}')
print(f'Notas de R$5: {cedula5}')
print(f'Notas de R$1: {cedula1}')
print(f'\033[1;35m{enfeite}\033[m')
