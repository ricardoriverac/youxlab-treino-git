#Valor das viajens 
km=int(input('Sua viajem tem qunantos km?:'))
if km<=200:
    valor1= km*0.50
    print('O valor da sua viajem é de {:.2f}'.format(valor1))
else:
    valor2= km*0.45
    print('O valor da sua viajem é de {:.2f}'.format(valor2))