print('Bem vindo a baladinha!')
senha = int(input('digite a senha para entrar, dica: está entre 4 e 6'))
while senha != 5:
   print('senha errada') 
   senha = int(input('tente de novo!, dica: está entre 4 e 6')) 
else:
   print('senha correta!')


idade = int(input('Qual sua idade?'))

if idade >= 18:
   print('Você é maior de idade')

else:
   print('Você não possui a idade suficiente para passar!')

