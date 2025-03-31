#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
#preço normal e condição de pagamento:
# a vista dinheiro/cheque: 10% de desconto
# a vista no cartao: 5% de desconto
# em ate 2x no cartao: preço normal
#3x ou mais no cartao 20% de juros

produto = 1500

print("Escolha a sua forma de pagamento:")
print("1 - À vista (dinheiro/cheque) [10% de desconto]")
print("2 - À vista no cartão [5% de desconto]")
print("3 - Em até 2x no cartão [preço normal]")
print("4 - 3x ou mais no cartão [20% de juros]")

formaDePagamento = input("Digite o número da opção desejada: ")

if formaDePagamento == "1":
    valorFinal = produto * 0.90
    print("Voce pagará R${:.2f}, a vista em dinheiro/cheque.".format(valorFinal))
elif formaDePagamento == "2":
    valorFinal = produto * 0.95
    print("Voce pagará R${}, a vista no cartão.".format(valorFinal))

elif formaDePagamento == "3":
    valorFinal = produto
    print("Voce pagará R${}, parcelado em até 2x no cartão.".format(valorFinal))

elif formaDePagamento == "4":
    parcelas = int(input("Quantas parcelas, voce deseja pagar? (3 ou mais): "))

    if parcelas >= 3:
        valorFinal = produto * 1.20
        valorParcela = valorFinal / parcelas
        print("Voce pagará R${}, em {}x de R${:.2f}".format(valorFinal, parcelas, valorParcela))
    else: print("Opção inválida! Para essa escolha, as parcelas devem ser 3 ou mais.")
else: print("Opção inválida! Escolha um número entre 1 e 4.")