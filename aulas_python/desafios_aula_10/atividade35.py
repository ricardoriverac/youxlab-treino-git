print('-=-=-=-Será que os números que digitará formam um triângulo?-=-=-=-')
numero = float(input('Primeiro segmento: '))
numero2 = float(input('Segundo segmento: '))
numero3 = float(input('Terceiro segmento: '))

if numero3 < (numero + numero2):
    print('Ele forma um triângulo :)')
    
else:
    print('Ele não forma um triângulo :(')
