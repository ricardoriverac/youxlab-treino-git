print('=-'*20)
print('Bem-Vindo ao Banco RP')
print('=-'*20)
print('''Temos 
        NADA''')
valor=int(input('Qual o valor do saque?  '))
total=valor
ced=50
totced=0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced >0:
            print(f'Total de {totced} cedulas  de R${ced}')
        if ced == 50:
            ced=20
        elif ced ==20:
            ced = 10
        elif ced ==10:
            ced =1
        totced=0
        if total ==0:
            break
print('-'*15)
print('volte sempre ')