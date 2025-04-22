# def aumentar(preco, taxa, formato=False):
#     res = preco + (preco * taxa / 100)
#     return moeda(res) if formato else res

# def diminuir(preco, taxa, formato=False):
#     res = preco - (preco * taxa / 100)
#     return moeda(res) if formato else res

# def dobro(preco, formato=False):
#     res = preco * 2
#     return moeda(res) if formato else res

# def metade(preco, formato=False):
#     res = preco / 2
#     return moeda(res) if formato else res

# def moeda(preco):
#     return f'R${preco:.2f}'

# def dolar(valor, cotacao):
#     """Converte o valor de real para dólar com uma cotação padrão (pode ser alterada)."""
#     return f'US$ {valor / cotacao:.2f}'


# def resumo(valor=0, aum=0, redu=0):
#     print('-' * 35)
#     print(f'{"RESUMO DO VALOR":^35}')
#     print('-' * 35)
#     print(f'{"Preço analisado:":25}{moeda(valor)}')
#     print(f'{"Dobro do preço:":25}{dobro(valor, True)}')
#     print(f'{"Metade do preço:":25}{metade(valor, True)}')
#     print(f'{f"{aum}% de aumento:":25}{aumentar(valor, aum, True)}')
#     print(f'{f"{redu}% de redução:":25}{diminuir(valor, redu, True)}')
#     print('-' * 35)