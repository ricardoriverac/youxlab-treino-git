produto = float(input('preço do produto: '))
choice = int(input(''' escolha uma forma de pagamento: 
    [1] à vista dinheiro/cheque
    [2] à vista cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão
    Escolha: '''))
if choice == 1:
    desconto = produto*10/100
    print(f'o desconto vai ser de: R${desconto}')
elif choice == 2:
    desconto2 = produto*5/100
    print(f'o desconto vai ser de: R${desconto2}')
elif choice == 3:
     print(f'o desconto vai ser de: R${produto}')
else:
    desconto3 = produto*20/100
    juros = produto + desconto3
    print(f'o valor do pagamento vai ser de: R${desconto3}')