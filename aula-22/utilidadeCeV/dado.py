# def leiaDinheiro(pergunta):
#     while True:
#         n = input(pergunta).strip()
#         n.replace('.',',')
#         if n.replace('.',',').isdigit:
#             return float(n)
#         else: 
#             print(f'ERRO: "{n}" é um preço inválido')

# CÓDIGO ACIMA FOI A TENTAIVA...


def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print(f'ERRO: "{entrada}" é um preço inválido.')