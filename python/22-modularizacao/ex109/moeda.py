def metade(v , fort=False):
    num = v/2
    if fort:
        return formatar(num)
    return num
def dobro(v, fort=False):
    num = v*2
    if fort:
        return formatar(num)
    return num
def aumentar(v,n=0, fort=False):
    num = v + (v * n/100)
    if fort:
        return formatar(num)
    return num
def diminuir(v,n=0, fort=False):
    num = v - (v * n/100)
    if fort:
        return formatar(num)
    return num
def formatar(preco=0 , moeda='R$'):
    return f"{moeda}{preco:>.2f}".replace('.',',')

#solucao guanabara
# def metade(v , fort=False):
#   num = v/2
#   return num if fort is false else formatar(num)
#