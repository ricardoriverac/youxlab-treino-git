from ex112.utilidadesCeV.dados import dado, moedas



try:
    num = dado.leia_dinheiro()
    porcent1 = int(input('Por quanto você quer aumentar o valor? '))
    porcent2 = int(input('Por quanto você quer diminuir o valor? '))
    moedas.resumo(num, porcent1, porcent2)

except ValueError as erro:
    print(f'Erro {erro}')



import re

# def ler_valor_monetario():
#     while True:
#         entrada = input("Digite um valor monetário (ex: 1.234,56): ").strip()
        
#         # Regex para validar formato monetário brasileiro (com ou sem milhar, opcional R$)
#         if re.fullmatch(r'(R\$ )?\d{1,3}(\.\d{3})*(,\d{2})?', entrada):
#             # Remove "R$" e pontos, troca vírgula por ponto
#             valor_limpo = entrada.replace('R$', '').replace('.', '').replace(',', '.').strip()
#             try:
#                 return float(valor_limpo)
#             except ValueError:
#                 pass  # em teoria não deve ocorrer por causa da regex
#         else:
#             print("Valor inválido. Tente novamente.")

# # Exemplo de uso
# valor = ler_valor_monetario()
# print(f"Valor lido: R$ {valor:.2f}")