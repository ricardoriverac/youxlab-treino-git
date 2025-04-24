from datetime import date
atual = date.today().year
totaldeMaior = 0
totaldeMenor = 0
for c in range(1,8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}° pessoa '))
    idade = atual - nascimento
    if idade >= 18 :
        totaldeMaior += 1
    else:
        totaldeMenor += 1
print(f'O total de maior de idade foi {totaldeMaior}')
print(f'O total de menor de idade foi {totaldeMenor}')
