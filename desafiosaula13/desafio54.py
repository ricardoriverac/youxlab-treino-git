import datetime
ano = datetime.date.today().year
maior = 0
menor = 0
for c in range (0, 7):
    anoN = int(input('Qual o ano do seu nascimento? '))
    conta = ano-anoN
    if conta>18:
        maior+=1
    else:
        menor+=1
print ('A quantidade de pessoas que atingiram a maioridade é {} '.format(maior))
print('A quantidade de pessoas que ainda não atingiram a maioridade é {}'.format(menor))