print('-=-=-=-Será que os números que digitará formam um triângulo?-=-=-=-')
numero1 = float(input('Primeiro segmento: '))
numero2 = float(input('Segundo segmento: '))
numero3 = float(input('Terceiro segmento: '))

if numero1 < numero2 + numero3 and numero2 < numero1 + numero3 and numero3 < numero2 + numero1 :
    print('Ele forma um triângulo :)')
    
else:
    print('Ele não forma um triângulo :(')
