#Esreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Qual velocidade seu veiculo atingiu? "))

multa = (vel-80)*7

if vel > 80:
    print("Voce tomou multa de R${:.2f}".format(multa))
else: 
    print("Voce anda no limite.")