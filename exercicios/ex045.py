import random
jokenpo= int(input('Escolha um número de 1 a 3: \n 1 para pedra \n 2 para papel \n 3 para tesoura \n Digite aqui: '))
if jokenpo == 1:
  lista= [1,2,3]
  jogo1= jokenpo == random.shuffle(lista)
  print(jogo1)