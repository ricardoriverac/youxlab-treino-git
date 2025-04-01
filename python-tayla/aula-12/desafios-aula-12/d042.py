reta1 = float(input('Digite o valor de uma reta: '))
reta2 = float(input('Digite o valor de outra reta: '))
reta3 = float(input('Digite o valor de outra reta: '))
if reta1 == reta2 and reta1 == reta3:
    print('As três retas formam um triângulo equilátero')
elif reta1 != reta3 and reta1 != reta2:
    print('As três retas formam um triângulo escaleno')
elif reta1 == reta2 or reta2 == reta3:
    print('As três retas formam um triângulo isósceles')
else:
    print('As três retas não formam um triângulo')