print('===' * 20)
print("""LOJA DOS YOUXERS
    .Temos Inovação
    .Preços acessiveis
    .Uma boa comida
    .Otimo funcionarios
VENHAS NOS CONHECER EM LAVRAS MG            """)
print('===' * 20)
print("""Tipos de Pagamento
    [ 1 ]- A vista(chegue/dinheiro) é olha so, 10% de desconto pra vocẽ
    [ 2 ]- A vista no cartão , e so pra você 5% de desconto
    [ 3 ]- Em 2x no cartão , so que sem desconto ;-;
    [ 4 ]- Em 3x no cartão , 20x de juros """)
print('===' * 20)

valor=float(input('Qual o falor do produto? '))
op=int(input('Qual forma de pagamento deseja pagar? '))
if op == 1:
    op1= valor - (valor * 10/100)
    print('A vista com um desconto de 10% fica {}'.format(op1))
elif op ==2:
    op2= valor - (valor * 5/100)
    print('No cartão com 5% de desconto fica {}'.format(op2))
elif op == 3:
    op3= valor / 2
    print('O seu produto fica em 2x em {}'.format(op3))
elif op ==4:
    op3= valor + (valor * 20/100)
    prc=int(input('Em quantas vezes quer pagar? '))
    ttl= op3 /prc
    print('Sua compra sera de {} e parcelado em {}'.format(prc , ttl))
print('Sua compra  de R${:.2f} vai ficar em {:.2f}'.format(valor , op3))    
print('-=-' * 20)
print("""Obrigado pela compra : Com prazer Youx""")
print('¨¨_¨¨' * 20)




