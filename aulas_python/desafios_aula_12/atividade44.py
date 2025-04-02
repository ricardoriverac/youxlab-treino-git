print('========== LOJA DO GARÇA ==========')
preco = float(input('Preço das compras: R$'))
print('Formas de pagamentos\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão' )
opcao = int(input('Qual a opção? '))

#variaveis :)
vista = (10/100*preco)
subtracao1 = preco-vista

vistac = (5/100*preco)
subtracao2 = preco-vistac

xcartao = preco/2 


if opcao == 1:
    print('Você terá que pagar R${}'.format(subtracao1))
    
elif opcao == 2:
    print('Você terá que pagar R${}'.format(subtracao2))
    
elif opcao == 3:
    print('Você terá que pagar R${} durante 2 meses'.format(xcartao))
    
elif opcao == 4:
    vezes= int(input('Em quantas vezes quer dividir sua compra? '))
    xtcartao = preco*1.20/vezes
    print('Sua compra ficará R${} durante {} meses'.format(xtcartao, vezes))
print('========== OBRIGADO PELA PREFERÊNCIA ==========\n========== VOLTE SEMPRE! ==========')