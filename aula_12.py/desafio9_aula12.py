preco = float(input("Informe o preço do produto: R$"))
print("O preço do produto é:{}".format(preco))
print("""
[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista no cartão: 5% de desconto
[3] - Em até 2X no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros""")
opcaoPagamento = int(input("Informe a opção de pagamento:"))
if opcaoPagamento == 1:
    precoAtualizado = preco - (preco*0.10)
    print("O preço atual é: R${}".format(precoAtualizado))
elif opcaoPagamento == 2:
    precoAtualizado = preco - (preco*0.05)
    print("O preço atual é: R${}".format(precoAtualizado))
elif opcaoPagamento == 3:
    precoAtualizado = preco
    print("O preço atual é: R${}".format(precoAtualizado))
elif opcaoPagamento == 4:
    precoAtualizado = preco + (preco*0.2)
    print("O preço atual é: R${}".format(precoAtualizado))