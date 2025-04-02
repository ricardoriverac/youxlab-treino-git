print('ME DIGA O COMPRIMENTO DE TRÊS RETAS')
primeiroLado = float(input('Reta 1: '))
segundoLado = float(input('Reta 2: '))
terceiroLado = float(input('Reta 3: '))
if primeiroLado == segundoLado == terceiroLado:
    print('O triângulo é {}EQUILÁTERO{}, pois todos os lados são iguais '.format('\033[35m', '\033[m'))
elif primeiroLado == segundoLado or segundoLado == terceiroLado or primeiroLado == terceiroLado:
    print('O triângulo é {}ISÓSCELES{}, pois dois lados são iguais '.format('\033[35m', '\033[m'))    
elif primeiroLado != segundoLado != terceiroLado:
    print('O triângulo é {}ESCALENO{}, pois todos os lados são diferentes '.format('\033[35m', '\033[m'))
    