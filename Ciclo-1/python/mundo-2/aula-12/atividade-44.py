produto = float(input('valor do produto: '))
escolha = int(input('''opção de pagamento: 
1 a vista no dinheiro
2 a vista no cartão
3 2x no cartão
4 3x ou mais no cartão
: '''))
if escolha == 1:
 pagamento1 = produto*10/100
 print(f'o valor com desconto ser R${pagamento1} ')
elif escolha == 2:
 pagamento3 = produto*5/100
 print(f'o valor com desconto ser R${pagamento2}')
elif escolha == 3 :
 print(f'o valor vai ser R${produdo} ')
elif escolha == 4:
 pagamento4 = produto*20/100
 juros = produto+pagamento4
 print(f'o valor sera de R${juros}')