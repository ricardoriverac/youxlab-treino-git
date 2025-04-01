print ('ME DIGA O COMPRIMENTO DE 3 RETAS')
primeiraReta = float(input('Reta 1: '))
segundaReta = float(input('Reta 2: '))
terceiraReta = float(input('Reta 3: '))
if primeiraReta + segundaReta > terceiraReta and segundaReta + terceiraReta > primeiraReta and terceiraReta + primeiraReta > segundaReta:
    print('Com essas retas É POSSÍVEL formar um triângulo! ')
else:
    print('Com essas retas NÃO É POSSÍVEL fazer um triângulo! ')
