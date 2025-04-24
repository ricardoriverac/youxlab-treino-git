def metade(preco, formato=False):
    resultado = preco / 2
    return resultado if formato else resultado

def dobro(preco, formato=False):
    resultado = preco * 2
    return resultado if formato else resultado

def aumentar(preco, porcentagem, formato=False):
    resultado = preco + (preco * porcentagem / 100)
    return resultado if formato else resultado
