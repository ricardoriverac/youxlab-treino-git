# def formato(valor):
#     return f'R$ {valor:.2f}'.replace('.', ',')

# def metade(valor, formatar=False):
#     resultado = valor / 2
#     return formato(resultado) if formatar else resultado

# def dobro(valor, formatar=False):
#     resultado = valor * 2
#     return formato(resultado) if formatar else resultado

# def aumentar(valor, percentual, formatar=False):
#     resultado = valor * (1 + percentual / 100)
#     return formato(resultado) if formatar else resultado

# def diminuir(valor, percentual, formatar=False):
#     resultado = valor * (1 - percentual / 100)
#     return formato(resultado) if formatar else resultado

# def converter_para_dolar(valor, taxa_cambio, formatar=False):
#     resultado = valor / taxa_cambio
#     return f'US$ {resultado:.2f}'.replace('.', ',') if formatar else resultado

# def resumo(valor, taxa_cambio):
#     """
#     Exibe um resumo com as operações sobre o valor:
#     metade, dobro, aumento, redução e conversão para dólar.
#     """
#     print("\n--- RESUMO DO VALOR ---")
#     print(f"Preço analisado: {formato(valor)}")
#     print(f"Metade: {metade(valor, True)}")
#     print(f"Dobro: {dobro(valor, True)}")
#     print(f"Aumento de 10%: {aumentar(valor, 10, True)}")
#     print(f"Redução de 13%: {diminuir(valor, 13, True)}")
#     print(f"Convertido para Dólar: {converter_para_dolar(valor, taxa_cambio, True)}")
#     print('-'*50)
