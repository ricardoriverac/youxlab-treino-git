#escreva um programa para aprovar um empréstimo banário para a compra de uma casa, 
# o programa vai perguntar o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação sabendo que que ela não pode exceder 30% do salario ou então
#emprestimo será negado

casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salário?'))
anos = float(input('Em quantos anos você vai pagar?'))
prestação = casa / (anos * 12)
minimo = salario * 30 /100

if prestação <= minimo:
    print('Empréstimo APROVADO!')
    print('Para pagar uma casa de R${} e em {} anos você pagará a prestação de {}'.format(casa, anos, prestação))
else:
    print('Empréstimo NEGADO!!')

