print ('ME DIGA O COMPRIMENTO DE 3 RETAS')
primeiraReta = float(input('Reta 1: '))
segundaReta = float(input('Reta 2: '))
terceiraReta = float(input('Reta 3: '))
if primeiraReta + segundaReta > terceiraReta and segundaReta + terceiraReta > primeiraReta and terceiraReta + primeiraReta > segundaReta:
    print('Com essas retas É POSSÍVEL formar um triângulo! ')
else:
    print('Com essas retas NÃO É POSSÍVEL formar um trângulo! ')

if primeiraReta == segundaReta == terceiraReta:
        print('O triângulo é {}EQUILÁTERO{}, pois todos os lados são iguais '.format('\033[35m', '\033[m'))   

elif primeiraReta != segundaReta != terceiraReta !=primeiraReta:
        print('O triângulo é {}ESCALENO{}, pois todos os lados são diferentes '.format('\033[35m', '\033[m'))
        
else:
        print('O triângulo é {}ISÓSCELES{}, pois dois lados são iguais '.format('\033[35m', '\033[m')) 
        
