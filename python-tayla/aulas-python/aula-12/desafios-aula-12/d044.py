valor = float(input('Digite o valor do produto: R$'))
print(""" escolha a forma de pagamento
[1] dinheiro/cheque
[2] cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")

#variaveis pra achar o valor
dinheiro = (valor * 0.10) - valor
cartao = (valor * 0.05) - valor
cartao3 = (valor * 0.20) + valor

#mostrando resultado
opcao = int(input('Escolha a forma de pagamento '))
if opcao == 1:
    print(f'O valor a ser pago é R${dinheiro:.2f}')
elif opcao == 2:
    print(f'O valor a ser pago é R${cartao:.2f}')
elif opcao == 3:
    print(f'O valor a ser pago é R${valor:.2f}')
else:
    print(f'O valor a ser pago é R${cartao3:.2f}')