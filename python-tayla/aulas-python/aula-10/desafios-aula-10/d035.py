reta1 = float(input('Digite o valor de uma reta: '))
reta2 = float(input('Digite o valor de outra reta: '))
reta3 = float(input('Digite o valor de outra reta: '))
if reta1 > (reta2 + reta3) or reta2 > (reta1 + reta3) or reta3 > (reta1 + reta2):
    print('As três retas formam um triângulo')
else:
    print('As três retas não formam um triângulo')