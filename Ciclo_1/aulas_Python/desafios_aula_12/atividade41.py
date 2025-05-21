from datetime import datetime
print('-=-=-=-=-Bem vindo(a) a CNN-=-=-=-=-')
ano = int(input('Qual seu ano de nascimento? '))

ano_atual = datetime.now().year

idade = ano_atual- ano

if idade <= 9:
    print('Você está na categoria: MIRIM')
    
elif 9 < idade <= 14:
    print('Vocẽ está na categoria: INFANTIL')
    
elif 14 < idade <= 19:
    print('Você está na categoria: JUNIOR')
    
elif 19 < idade <= 20:
   print('Você está na categoria: SÊNIOR')
    
elif idade > 20:
   print('Você está na categoria: MASTER')