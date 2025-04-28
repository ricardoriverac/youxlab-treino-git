tot18 = totH = totM20 = 0

print('-'*20)
print('CADASTRE UM PLAYER')
print('-'*20)

while True:
    idade = int(input('Digite sua Idade '))
    sexo =  ' '
    while sexo  not in 'MF':
        sexo = str(input('Digite seu sexo ')).strip() . upper()
        print('-='*10)
    if idade >18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    
    responda = ' '
    while responda not in 'SN':
        responda = str(input('Você quer continuar cadastrando pessoas? [S/N] ')).upper(). strip()
        print('-='*20)
    if responda == 'N':
        break
print(f'O total de pessoas maior de idade é {tot18}')
print('-'*20)
print(f'O total de homens é {totH}')
print('-'*20)
print(f'O total de Mulheres com menos de 20 anos é {totM20}')
                

    
            



