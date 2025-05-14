print ('<>' * 7)
print ('BANCO DO LABER')
print ('<>' * 7)

valor = int(input('Valor que deseja sacar: R$ '))

total = valor
cedula = 50
totalDeCedulas = 0

while True: 
    if total >= cedula: #Quantas vezes consigo tirar 50 desse valor
        total -= cedula
        totalDeCedulas += 1
    else:
        if totalDeCedulas > 0:
            print (f'Total de {totalDeCedulas} nota(s) de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        totalDeCedulas = 0
        if total == 0:
            break

print ('<>' * 25)
print ('Volte sempre ao caixa eletrônico do BANCO DO LABER!')
print ('Tenha um Bom Dia!')
print ('<>' * 25)