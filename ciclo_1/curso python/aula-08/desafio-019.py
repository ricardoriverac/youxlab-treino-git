import random
aluno1 = str(input('qual o nome do primeiro aluno'))
aluno2 = str(input('qual o nome do segundo aluno?'))
aluno3 = str(input('qual o nome do terceiro aluno?'))
aluno4 = str(input('qual o quarto aluno?'))

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)

print ('o aluno escolhido foi: {}'.format(sorteio))

#import random
#num = random.randint(1, 4)

#aluno1 = Pedro 
#luno2 = Mateus
#aluno3 = Lucas
#aluno4 = Maria

#if aluno1 ==1:
  #  print('O aluno {} foi escolhido'.format(aluno1))
#else: 

#if aluno2 ==2:
 #   print(' O aluno {} foi escolhido'.format(aluno2))
#else: 

#if aluno3 ==3:
 #   print('o aluno {} foi escolhido'.format(aluno3))
#else:

#if aluno4 ==4:
 #   print('o aluno {} foi escolhido'.format(aluno4))
#else:

