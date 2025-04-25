def aumentar(numero = 0, x = 0):
    numero += (numero * (x / 100))
    return numero

def metade(numero = 0):
    numero /= 2
    return numero

def dobro(numero = 0):
    numero *= 2
    return numero

def linha():
    print('-=' * 15)

def moeda(numero = 0, moeda = 'R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')