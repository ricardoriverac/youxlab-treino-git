from datetime import date
menor=0
maior=0
anoAtual=date.today().year
for pes in range(1,4):
    ano=int(input('Em que ano você nasceu ? '))
    idade = anoAtual - ano

    if idade <=17:
       menor +=1
    else:
        maior +=1

print('Ao todo tivemos {} pessoas maiores.E também tivemos {} pessoas menores de idade '.format(maior,menor))




    
