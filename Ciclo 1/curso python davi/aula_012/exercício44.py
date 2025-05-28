print('lojinha do davizão')
preço = float(input('preço das compras: '))
print (''' Formas de pagamento
[ 1 ]a vista dinheiro
[ 2 ]a vista cartão 
[ 3 ]2x no cartão
[ 4 ]3x ou mais no cartão''')
opção = int(input('qual a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100 )
elif opção == 3:
    total = preço
    parcela = total / 2
    print('sua conta será parcelada em 2x de {:.2f}' .format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalprc = int(input('quantas parcelas?'))
    parcela = total / totalprc
print(' sua compra será parcelada em {}x de {:.2f} com juros '.format(totalprc, parcela))
     
print('Sua compra de {:.2f} no total será {:.2f}' .format(preço, total))
