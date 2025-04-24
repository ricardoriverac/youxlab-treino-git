def notas():
    notas = []
    while True:
        nota = float(input('\033[1mDigite uma nota:\033[m '))
        notas.append(nota)

        while True:
            resposta = str(input('\033[2;36mQuer continuar?\033[3m [S/N]\033[m ')).upper()[0]
            if resposta in 'SN':
                break
            print('\033[4;31mDigite corretamente.\033[m', end=' ')

        if resposta == 'N':
            break

    return notas 
def linha():
    from time import sleep
    texto = 'VAMOS VER AS NOTAS DA TURMA'
    print('\033[3;37m=\033[m' * len(texto))
    sleep(0.5)
    print(f'\033[3;34m{texto}\033[m')
    sleep(0.5)
    print('\033[3;37m=\033[m' * len(texto))

linha()
from time import sleep
todas_notas = notas()
dic = {}
dic['notas'] = todas_notas
quantidade = len(todas_notas)
maior = max(todas_notas)
menor = min(todas_notas)
soma = sum(todas_notas)
media = soma/quantidade
print(f'\033[3;30mNotas digitadas:\033[1m {dic}\033[m')
sleep(0.5)
print(f'\033[3;30mA quantidade de notas digitadas foi\033[1;34m {quantidade}\033[m')
sleep(0.5)
print(f'\033[3;30mA maior nota foi\033[1;34m {maior}\033[3;30m e a menor foi \033[1;34m{menor}\033[m')
sleep(0.5)
print(f'\033[3;30mA média das notas foi \033[1;34m{media:.2f}\033[m')
sleep(0.5)

if media > 7.0:
    dic["situação"] = 'BOA}'
if media >=6.0 and media <=6.9:
    dic['situação'] = 'RAZOÁVEL'
if media < 6.0:
    dic['situação'] = 'HORRÍVEL'

print(dic)