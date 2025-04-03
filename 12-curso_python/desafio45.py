import random
from time import sleep
print ('Vamos jogar pedra, papel e tesoura?')
sleep(2)
minhaEscolha = ('Escolha pedra, papel ou tesoura: ')
lista = ['pedra', 'papel', 'tesoura']
print('Escolha uma opção: ')
pedra = print('[1] Pedra')
papel = print('[2] Papel')
tesoura = print('[3] Tesoura')
escolha = int(input('Escolha sua opção: '))
computador = random.choice(lista)
print ('O computador escolheu {}.'.format(computador))
if computador ==1 and escolha ==2 or computador ==2 and escolha ==3 or computador ==3 and escolha ==1 :
    print('Parabéns, você ganhou!')
elif computador ==1 and escolha ==1 or computador ==2 and escolha ==2 or computador ==3 and escolha ==3 :
    print('Vocẽs empataram.')
else :
    print('VOCÊ PERDEU MUHAHAHAHA')