#Escreva um programa para aprovar o emprestimos bancario para comprar de uma casa.
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode execeder 30% do salario
#Ou então o emprestimo será negado.

casa = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o seu salario? "))
anos = int(input("Quantos anos, voce pretende pagar? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print("Emprestimo aprovado")
else: print("Emprestimo negado")