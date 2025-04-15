velocidade = int(input('Digite a velocidade do carro: '))
multa = velocidade * 7
if velocidade > 80:    
    print (f'Você foi multado! O valor a pagar é de R${multa} ')
else:
    print ('Não há multa para pagar. Siga em frente! ')