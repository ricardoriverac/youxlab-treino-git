lista =[ ]
somaIdade = 0
mediaIdade = 0
maiorIdade = 0
nomedoVelho = ' '
totalMulher20 = 0
for pessoas in range(1, 5):
  print('::::::::::{}° PESSOA::::::::::::'.format(pessoas))
  print (' ')
  nomes = input(str('Digite o \033[1;33mNOME \033[0;0mda {} pessoa: '.format(pessoas))).strip()
  idade = int(input('Digite a \033[1;31mIDADE \033[0;0mda {} pessoa: '.format(pessoas)))
  sexo = input(str('Digite o \033[1;35mGENÊRO \033[0;0mda {} pessoa[M/F]: '.format(pessoas))).strip()
  print(' ')
  somaIdade += idade 
  if pessoas ==1 and sexo in 'Mm':
   maiorIdade = idade
   nomedoVelho = nomes 
  if sexo in 'Mm' and idade > maiorIdade :
   maiorIdade = idade
   nomedoVelho = nomes
  if sexo in 'Ff' and idade>20 :
   totalMulher20 +=1


mediaIdade = somaIdade / 4


print ('A média da idade do grupo é: {}'.format(mediaIdade))
print ('O homem mais velho se chama {} e sua idade é {}'.format(nomedoVelho, maiorIdade) )
print ('Nesse grupo tem {} mulheres com mais de 20 anos.'.format(totalMulher20))