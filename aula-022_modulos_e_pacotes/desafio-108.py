from ex107 import moedas
from time import sleep
num = float(input('Digite um numero: '))
porcent = int(input('Digite um número: '))
print(f'O dobro de {num} é {moedas.dobro(num)}')
print(f'A metade de {num} é {moedas.metade(num)}')
print(f'O aumento de {num} em {porcent}% é {moedas.aumentar(num, porcent)}')
print(f'A redução em {num} em {porcent}% é {moedas.diminuir(num, porcent)}')
print(moedas.outraMoeda(num, porcent))
while True:
    print('-=' * 30)
    print('Tabela:')
    print('-=' * 30)
    print('\n [D] Dolar \n [R] Real \n [B] binario \n ')
    print('-=' * 30)
    conv = str(input('Para qual moeda você quer converter? ')).upper()
    print(moedas.outraMoeda(num, conv))
    continuar = str(input('Quer continuar? (S/N)')).upper()
    if continuar == 'N':
        break