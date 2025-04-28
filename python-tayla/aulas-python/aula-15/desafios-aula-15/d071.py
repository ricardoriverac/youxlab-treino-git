cedulas = 50
quantidade = 0

print('=' * 17 )
print('    BANCO LAB    ')
print('=' * 17)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor

while True:
    if total >= cedulas:
        total -= cedulas
        quantidade += 1
        
    else:
        if quantidade > 0:
            print(f'Total de {quantidade} cédulas de R${cedulas}')

        if cedulas == 50:
            cedulas = 20

        elif cedulas == 20:
            cedulas = 10

        elif cedulas == 10:
            cedulas = 1
        quantidade = 0

        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO LAB!')