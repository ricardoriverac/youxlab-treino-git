import datetime

ano = int(input('Ano do Nascimento do Atleta:'))

agora = datetime.datetime.now()

data_atual = agora.year

idade = data_atual - ano

if idade <= 9:
    print('Categoria MÍRIM')

elif idade <= 14: 
    print('Categoria INFANTIL')  

elif idade <= 19:    
    print('Categoria JUNIOR')

elif idade <= 20:    
    print('Categoria SÊNIOR')

else: 
    print('Categoria Mater')