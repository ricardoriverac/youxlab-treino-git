reta1 = float(input('reta 1: '))
reta2 = float(input('reta 2: '))
reta3 = float(input('reta 3: '))
if (reta1 + reta2 < reta3) or (reta1 + reta3 < reta2) or (reta2 + reta3 < reta1):
        print('Nao é um triangulo')
elif (reta1 == reta2) and (reta1 == reta3):
        print('Equilatero')
elif (reta1==reta2) or (reta1==reta3) or (reta2==reta3):
        print('Isósceles')
else:
        print('Escaleno')
