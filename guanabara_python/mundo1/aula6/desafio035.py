reta1 = float(input('reta 1: '))
reta2 = float(input('reta 2: '))
reta3 = float(input('reta 3: '))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('você pode fazer um triângulo com esses valores')
else:
    print('não dá para fazer um trângulo')