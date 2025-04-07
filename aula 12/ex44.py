preco = float (input ("Valor do produto: "))
print("""Digite a opção do pagamento: 
[1] à vista dinheiro ou cheque, 10% de desconto. 
[2] à vista no cartão, 5% de desconto.
[3] em até 2 vezes no cartão, preço normal.
[4] 3x ou mais no cartão, 20% juros.
      """)
pagamento = int (input ("Opção de pagamento escolhida: "))
if pagamento == 1 :
    valorfinal = preco - (preco * 10 / 100)
    print ("À vista dinheiro ou cheque, 10% de desconto. ")
    print ("O preço do produto foi \033[33m{}\033[m , valor final \033[33m{}\033[m ".format(preco,valorfinal))
elif pagamento == 2 :
    valorfinal = preco - (preco * 5 / 100)
    print ("à vista no cartão, 5% de desconto.")
    print ("O preço do produto foi \033[33m{}\033[m , valor final \033[33m{}\033[m ".format(preco,valorfinal))
elif  pagamento == 3 :
    print ("Preço normal! ")
    print ("O preço do produto foi \033[33m{}\033[m ".format(preco))
elif pagamento == 4 :
    print ("3x ou mais no cartão, 20% juros.")
    valorfinal = preco + (preco * 20 / 100)
    vezes = float (input("Em quantas parcelas: "))
    parcela = valorfinal/vezes
    print ("Você dividiu em \033[33m{}\033[m X com juros. ".format(parcela))
    print ("O preço do produto foi \033[33m{}\033[m , valor final \033[33m{}\033[m ".format(preco,valorfinal))