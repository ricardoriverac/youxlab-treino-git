#módulo moeda.py que tem as funções incorporadas aumentar(), diminuir(), dobro(), metade() e moeda()

def aumentar(din, formato=False):
    if din:
        aumento = 15 / 100
        aumentoFinal = din + (din * aumento)
        if formato:
            return moeda(aumentoFinal)
        else:
            return aumentoFinal

def diminuir(din, formato=False):
    if din:
        desconto = 15 / 100
        descontoFinal = din - (din * desconto)
        if formato:
            return moeda(descontoFinal)
        else:
            return descontoFinal

def metade(din, formato=False):
    if din:
        metade = din / 2
        if formato:
            return moeda(metade)
        else:
            return metade

def dobro(din, formato=False):
    if din:
        dobro = din * 2
        if formato:
            return moeda(dobro)
        else:
            return dobro

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
