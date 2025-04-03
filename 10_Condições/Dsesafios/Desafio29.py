n1 = float(input("Qual e a velocidade do carro? "))
multa = n1 * 7
if n1 >= 80:
    print("Sua velocidade foi {}km/h,O limite era 80km/h,entao voce sera multado em {}R$".format(n1,multa))
else:
    print("Voce nao foi multado, pois sua velocidade {}km/h e menor que 80km/h".format(n1))