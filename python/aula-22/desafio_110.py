def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def dobro(valor, formato=False):
    resultado = valor * 2
    return moeda(resultado) if formato else resultado

def metade(valor, formato=False):
    resultado = valor / 2
    return moeda(resultado) if formato else resultado

def aumentar(valor, taxa, formato=False):
    resultado = valor + (valor * taxa / 100)
    return moeda(resultado) if formato else resultado

def diminuir(valor, taxa, formato=False):
    resultado = valor - (valor * taxa / 100)
    return moeda(resultado) if formato else resultado

def resumo_interativo():
    from time import sleep

    try:
        preço = float(input('Digite o preço: R$'))
        taxaa = float(input('Digite a taxa de AUMENTO (%): '))
        taxar = float(input('Digite a taxa de REDUÇÃO (%): '))
    except ValueError:
        print('\033[31mErro: Por favor, insira valores válidos!\033[m')
        return

    print('\033[31m-=' * 30)
    print('RESUMO DO VALOR'.center(60))
    print('\033[31m-=' * 30)

    print(f'\033[34mPreço analisado:\t{moeda(preço)}')
    sleep(1)
    print(f'\033[32mDobro do preço:\t\t{dobro(preço, True)}')
    sleep(1)
    print(f'\033[32mMetade do preço:\t{metade(preço, True)}')
    sleep(1)
    print(f'\033[32m{taxaa}% de aumento:\t{aumentar(preço, taxaa, True)}')
    sleep(1)
    print(f'\033[32m{taxar}% de redução:\t{diminuir(preço, taxar, True)}')
    sleep(1)
    print('\033[31m-=' * 30)
resumo_interativo()
