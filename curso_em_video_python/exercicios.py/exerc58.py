from random import randint

print ('Tente advinhar o número de 0 a 10..')

computador = randint(0, 10)
numero = int(input('Digite o número aqui: '))
erro = 0

if numero == computador :
    print('UAU você acertou!!')

while numero != computador:
    numero = int(input('Você errou, digite novamente: '))
    erro += 1


print('Parabéns. Até acertar você errou {} vezes.'.format(erro))
