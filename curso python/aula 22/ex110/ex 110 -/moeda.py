def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res

def dobro(preco=0, formato=False):
    res = preco * 2
    if formato:
        return moeda(res)
    else:
        return res

def metade(preco=0, formato=False):
    res = preco / 2
    if formato:
        return moeda(res)
    else:
        return res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, aumento=10, reducao=5):
    print('\n' + '\033[35m-\033[m'*40)
    print('\033[35mRESUMO DO VALOR\033[m'.center(30))
    print('\n' + '\033[35m-\033[m'*40)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(preco, aumento, True)}")
    print(f"{reducao}% de redução: \t{diminuir(preco, reducao, True)}")
    print('\n' + '\033[35m-\033[m'*40)
