reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
if reta1 == reta2 and reta1 == reta3:
    print ('Este é um triângulo Equilátero!. ')
elif reta1 == reta2 or reta1 == reta3:
    print ('Este é um triângulo Isósceles!. ')
elif reta1 != reta2 and reta1 != reta3:
    print ('Este é um triângulo Escaleno!. ')