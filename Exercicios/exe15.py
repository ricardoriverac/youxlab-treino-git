#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,75 por KM rodado.

dias = int(input("Quantos dias você alugou o carro? "))
kmRodados = float(input("Quantos km você percorreu com o carro? "))

valorTotal = (dias * 60) + (kmRodados * 0.15)

print("O valor total á pagar e de R${:.2f}.".format(valorTotal))