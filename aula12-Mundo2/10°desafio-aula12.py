from random import randint
from time import sleep
opcoes=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('VAMOS JOGAR JOKENPÔ?')
print('Escolha uma dessas opções:\n' \
'0-PEDRA\n' \
'1-PAPEL\n' \
'2-TESOURA')
escolha=int(input('Qual opção você quer?:'))
print('Você jogou:{}'.format(opcoes[escolha]))
print('Computador jogou:{}'.format(opcoes[computador]))
if computador==0:
 if escolha==0:
  print('EMPATE!')
 if escolha==1:
  print('VOCÊ GANHOU!')
 if escolha==2:
  print('VOCÊ PERDEU!')
if computador==1:
 if escolha==1:
  print('EMPATE!')
 if escolha==2:
  print('VOCÊ GANHOU!')
 if escolha==0:
  print('VOCÊ PERDEU!')
if computador==2:
 if escolha==2:
  print('EMPATE!')
 if escolha==1:
  print('VOCÊ GANHOU!')
 if escolha==0:
  print('VOCÊ PERDEU!')
  
  