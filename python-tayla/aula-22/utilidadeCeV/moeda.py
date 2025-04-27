def aumentar(numero = 0, x = 0, mostrar = False):
    numero += (numero * (x / 100))

    return numero if mostrar is False else moeda(numero)

def diminuir(numero = 0, x = 0, mostrar = False):
    numero -= (numero * (x / 100))

    return numero if mostrar is False else moeda(numero)

def metade(numero = 0, mostrar = False):
    numero /= 2

    return numero if mostrar is False else moeda(numero)

def dobro(numero = 0, mostrar = False):
    numero *= 2

    return numero if mostrar is False else moeda(numero)

def linha():
    print('-=' * 15)

def moeda(numero = 0, moeda = 'R$' ):
    return f'{moeda}{numero:.2f}'.replace('.', ',') 

def titulo():
    linha()
    print('\033[1;36m      RESUMO DO VALOR\033[m')
    linha()

def resumo(preco = 0, aumento = 0, reducao = 0):
    titulo()
    print(f'Preço analisado: {moeda(preco):>10}')
    print(f'Dodro do preço:   {dobro(preco, True):>10}')
    print(f'Metade do preço: {metade(preco, True):>10}')
    print(f'{aumento}% de aumento:  {aumentar(preco, aumento, True):>10}')
    print(f'{reducao}% de redução:  {diminuir(preco, reducao, True):>10}')