valor=int(input('Me diga o valor do produto:R$ '))
metodo=int(input(''' Me diga qual das formas de pagamento quer'
(1) Á vista dinheiro'
(2) Á vista no cartão'
(3) Pagar em até 5 vezes      
(4) Pagar em 6 ou mais parcelas '''))

if metodo == 1:
    print('O valor que você pagara a vista sera de {} '.format(valor))
elif metodo == 2:
    print('A vista no cartão havera um aumento de 5%, totalizando {} '.format(valor*5/100 +valor))
elif metodo ==3:
    print('Em ate 5 vezes você pagara apenas 10% mais ficando {} '.format(valor*10/100 +valor) )
elif metodo == 4:
    print('aparti de 6 vezes o total fica: {}'.format(valor*20+valor))


