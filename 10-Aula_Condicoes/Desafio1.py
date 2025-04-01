from random import randint
computador = randint(0 , 5)
print('-=-' * 20)
print('Vou pensar em numero entre  0 e 5. Tente adivinhar')
print('-=-' * 20)
jogador=int(input('em qual numero eu pensei?  '))
if jogador ==computador:
    print('Você Ganhou!!!!11')
else:
    print('Vocẽ Perdeu ')