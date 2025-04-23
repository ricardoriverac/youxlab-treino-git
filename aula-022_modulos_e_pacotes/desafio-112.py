from ex112.utilidadesCeV.dados import dado, moedas
try:
    num = dado.leia_dinheiro()
    porcent1 = int(input('Por quanto você quer aumentar o valor? '))
    porcent2 = int(input('Por quanto você quer diminuir o valor? '))
    moedas.resumo(num, porcent1, porcent2)

except ValueError as erro:
    print(f'Erro {erro}')





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


# def resumo(num, porcent1, porcent2):
#     dobro = num * 2
#     metade = num / 2
#     taxa = (porcent1/100) + 1
#     aumento = num * taxa
#     dimi = 1 - (porcent2/100)
#     diminui = num * dimi
#     print('-=' *30)
#     print('        RESUMO DO VALOR          ')
#     print('-=' *30)
#     print(f'A metade de {num} é {metade}')
#     print(f'O dobro de {num} é {dobro}')
#     print(f'O aumento em {porcent1} de {num} é {aumento}')
#     print(f'O valor reduzido em {porcent2} de num é {diminui}')
#     print('-=' *30)

# def leia_dinheiro(num):
#     isRodando = False
#     while not isRodando:
#         entrada = num.replace(',', '.').strip()
#         if entrada.isnumeric():
#             entrada = float(entrada)
#         if entrada.isalpha() or entrada == '':
#             raise ValueError (f'O valor {num} não é válido')
#         else:
#             isRodando = True
#             return print(f'O valor {num} é válido')



# try:
#     num = dado.leia_dinheiro(str(input('Digite um número: ')))

# except ValueError as erro:
#     print(f'Erro {erro}')


# porcent1 = int(input('Por quanto você quer aumentar o valor? '))
# porcent2 = int(input('Por quanto você quer diminuir o valor? '))
# moedas.resumo(num, porcent1, porcent2)