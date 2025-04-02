from datetime import datetime

anoatual = datetime.now().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    ano = int(input('Em que ano a pessoa {} nasceu? '.format(pess)))
    idade = anoatual - ano
    if idade>= 21:
        totmaior += 1
    else:
        totmenor +=1
print('Ao todo tivemos {} que são de maior '.format(totmaior))
print('E tivemos {} pessoas menores de idade '.format(totmenor))