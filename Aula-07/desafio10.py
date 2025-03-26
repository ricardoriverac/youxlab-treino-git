#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere US$1,00 = R$5,70

valorNaCarteira = float(input("Quantos de dinheiro, você possui na sua carteira? "))

valorDoDolar = 5.70

calculo = valorNaCarteira / valorDoDolar

print("Com R${:.2f}, você pode comprar US${:.2f}.".format(valorNaCarteira, calculo))