from datetime import date

anoatual = date.today().year 
ano = 0
maiores = 0   
menores = 0   

for i in range(0,7):
    ano = int(input('Digite o seu ano de nascimento:'))
    idade = anoatual - ano  
    if idade > 18:
        maiores = maiores + 1 
    else:
        menores = menores + 1  

print('Maiores de idade {} '.format(maiores))
print('Menores de idade {} '.format(menores))