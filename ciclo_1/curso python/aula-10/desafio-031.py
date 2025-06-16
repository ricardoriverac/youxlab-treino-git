#Faça um

print('Se os km/h forem abaixo de R$200.00 será cobrado 0.50 por km')
print('Se os km/h forem acima de R$200.00 será cobrado 0.45 por km')
km = float(input('Qual a distância da viagem?'))

if km <=200:
    print('O valor da viagem ficará em R${}'.format(km*0.50))
else:
    print('O valor da viagem ficará em R${}'.format(km*0.45))