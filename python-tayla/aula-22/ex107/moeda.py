def aumentar(numero, x):
    numero += (numero * (x / 100))
    return numero

def diminuir(numero, x):
    numero -= (numero * (x / 100))
    return numero

def metade(numero):
    numero /= 2
    return numero

def dobro(numero):
    numero *= 2
    return numero

def linha():
    print('-='* 15)