#módulo moeda.py que tem as funções incorporadas aumentar(), diminuir(), dobro() e metade()

def aumentar(din):
    if din:
        aumento = 15 / 100
        aumentoFinal = din + (din * aumento)
    return aumentoFinal

def diminuir(din):
    if din:
        desconto = 15 / 100
        descontoFinal = din - (din * desconto)
    return descontoFinal

def metade(din):
    if din:
        metade = din / 2
    return metade

def dobro(din):
    if din:
        dobro = din * 2
    return dobro