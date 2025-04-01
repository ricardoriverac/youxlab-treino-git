r1 = float(input('Digite um comprimento'))
r2 = float(input('Digite um comprimento'))
r3 = float(input('Digite um comprimento'))
#isoceles = num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM formar um triangulo!')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    
