from random import randint

computador = randint(0,5)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar')

pessoa = int(input('Digite o valor'))
if pessoa == computador:
    print('Você ganhou!!!')
else:
    print('Você é horrivel!!')