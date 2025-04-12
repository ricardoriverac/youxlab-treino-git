#módulo moeda.py que tem as funções incorporadas aumentar(), diminuir(), dobro(), metade(), moeda() e resumo()

def aumentar(din, formato=False, taxa=15):
    aumento = taxa / 100
    aumentoFinal = din + (din * aumento)
    if formato:
        return moeda(aumentoFinal)
    else:
        return aumentoFinal

def diminuir(din, formato=False, taxa=15):
    desconto = taxa / 100
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

def resumo(din, texto="RESUMO DO VALOR", aumento=10, reducao=5):
    largura = 40  # largura da tabela
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)
    print(f"Preço analisado: \t{moeda(din)}")
    print(f"Dobro do preço: \t{dobro(din, True)}")
    print(f"Metade do preço: \t{metade(din, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(din, True, aumento)}")
    print(f"{reducao}% de redução: \t{diminuir(din, True, reducao)}")
    print("~" * largura)
