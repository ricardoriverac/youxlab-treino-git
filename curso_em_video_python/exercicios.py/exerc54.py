from datetime import date
atual = date.today().year
maior = 0
menor = 0
for data in range (1,8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(data)))
    conta = atual - ano
    if conta > 18 :
        maior +=1
    else :
        menor +=1
print ('Ao todo temos {} pessoas maior de idade'.format(maior))
print ('E temos {} pessoas de menor.'.format(menor))