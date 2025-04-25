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