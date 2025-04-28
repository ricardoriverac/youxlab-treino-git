from  random import randint
valor=randint(0,5)
usuario= int(input('Me diga o numero que acha que sera sorteado por nossa máquina! '))
print('-'*20)
print('Nossa maquina escolheu o numero {} '.format(valor))
if  valor == usuario:
    print('Você acertou! ')
else: 
    print('Você errou!. O numero sorteado foi {} '.format(valor))

