valor=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual o seu salário? R$'))
anos=int(input('Em quantos anos você irá pagar a casa? R$'))
prestacao=valor/(anos*12)
minimo=salario*30/100
print('Para pagar uma casa de {:.2f} em {} anos,'.format(valor,anos))
print('o valor da prestaçao será de R${:.2f}'.format(prestacao))
if prestacao<=minimo:
    print('Empréstimo pode ser concedido. ')
else:print('Empréstimo negado!')