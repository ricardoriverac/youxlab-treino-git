vl = int(input('Qual é a velocidade do carro: '))
multa = (vl - 80) * 7.00
if vl > 80 :
    print(f'Limite ultrapassado à multa será de R${multa:.2f}')
elif vl == 80 :
    print('\033[0;35mBoa\033[m, muito bem está dirigindo nos limites')
else:
    print('Parabéns , Você está muito previnido')     