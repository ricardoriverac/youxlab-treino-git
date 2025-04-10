import random
jokenpo= int(input('Escolha um número de 1 a 3: \n 1 para pedra \n 2 para papel \n 3 para tesoura \n Digite aqui: '))
lista= [1, 2, 3]
jokenpo2= random.shuffle(lista)
print(jokenpo, jokenpo2)