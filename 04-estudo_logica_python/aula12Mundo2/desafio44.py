produto= float(input("Informe o preço do produto: R$"))
print("O preço do produto é:{}".format(produto))
print("""
[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista no cartão: 5% de desconto
[3] - Em até 2X no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros""")
pagamento = int(input("Informe a opção de pagamento:"))
if pagamento == 1:
    precoAtualizado = produto - (produto*0.10)
    print("O preço atual é: R${}".format(precoAtualizado))
elif pagamento == 2:
    precoAtualizado = produto- (produto*0.05)
    print("O preço atual é: R${}".format(precoAtualizado))
elif pagamento == 3:
    precoAtualizado = produto
    print("O preço atual é: R${}".format(precoAtualizado))
elif pagamento == 4:
    precoAtualizado = produto + (produto*0.2)
    print("O preço atual é: R${}".format(precoAtualizado))



