preco = float(input('Qual o preço normal do produto? '))

print('''Qual a forma de pagamento?
                         
[ 1 ] dinheiro a vista, 10 porcento de desconto
[ 2 ] cheque a vista, 10 porcento de desconto
[ 3 ] à vista no cartao, 5 porcento de desconto
[ 4 ] em até 2x no cartão, preço normal
[ 5 ] 3x ou mais no cartão, 20 porcento de juros''')

opcao=int(input('Sua opção: '))


if opcao == 1:
    p = preco - (preco * 0.10)
    print('Sua compra ficou R${} '.format(p))

elif opcao == 2:
    p = preco + (preco * 0.10)
    print('Sua compra ficou R${} '.format(p))

elif opcao == 3:
    p = preco - (preco / 20)
    print('Sua compra ficou R${}'.format(p))

elif opcao == 4:
    p = preco / 2
    print('Sua compra ficará com o valor de 2x de R${}'.format(p))

else:
    parcelas=int(input('Em quantas parcelas você irá pagar? '))
    pp = preco / parcelas 
    juros= preco * 0.20
    total= preco + juros
    print('''Você irá pagar {} parcelas de R${},
com aumento de 20 porcento de juros, que dá R${}, dando no total R$ {}'''.format(parcelas, pp, juros, total))