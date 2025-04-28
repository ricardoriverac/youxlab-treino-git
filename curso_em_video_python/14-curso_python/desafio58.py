# from random import randint

# print ('Tente advinhar o número de 0 a 10..')

# computador = randint(0, 10)
# numero = int(input('Digite o número aqui: '))
# erro = 0

# if numero == computador :
#     print('UAU você acertou!!')

# while numero != computador:
#     numero = int(input('Você errou, digite novamente: '))
#     erro += 1


# print('Parabéns. Até acertar você errou {} vezes.'.format(erro))

from random import randint

print ('Tente advinhar dois números de 1 a 10..')
erro = 0
computador = randint(1, 10)
computador2 = randint(1, 10)
numero = 0
numero2 = 0
isRodando = True

while isRodando :
    while numero != computador :
       numero = int(input('Digite o 1° número de novo aqui: '))
       erro +=1
       if numero == computador:
          print('Parabéns, você acertou o primeiro. Agora acerte o segundo.')
    while numero2 != computador2:
       numero2 = int(input('Digite o 2° número aqui:'))
       erro +=1
       if numero2 == computador2:
          print('AEEEEEE')
    isRodando = False
print('Parabéns. Até acertar você errou {} vezes.'.format(erro))

