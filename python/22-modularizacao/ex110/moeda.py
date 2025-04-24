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

def resumo(preco=0 , taxaa=10 , taxad=5):
    print('-'*30)
    print('ANALISANDO O VALOR'.center(30))
    print('-'*30)
    print(f'O preço analisado foi {formatar(preco)}')
    print(f'A metade do preço é {metade(preco , True)}')
    print(f'O dobro do preço é {dobro(preco, True)}')
    print(f'Aumentando o preço em {taxaa}% temos {aumentar(preco, taxaa , True)}')
    print(f'Diminuindo o preço em {taxad}% temos {diminuir(preco,taxad, True)}')