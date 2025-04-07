valor = float (input ("Qual o valor da casa ? "))
salario = float (input ("Quanto você recebe , seu salário ? "))
anos = int (input ("Em quantos anos você pagará a casa ? "))
prestacaomensal = valor / ( anos * 12)
minimo = salario * 3 / 100
print ("Você irá pagar em {} anos, o valor de R${}".format(anos, valor))
print ("A prestação será de R${}".format(prestacaomensal))
if  prestacaomensal <= minimo:
    print ("Emprestimo APROVADO !!")
else:
    print ("Emprestimo NÃO APROVADO !!!")