segmento1=float(input('Digite o valor do primeiro segmento:'))
segmento2=float(input('Digite o valor do segundo segmento:'))
segmento3=float(input('Digite o valor do terceiro segmento:'))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Esses segmentos formam um triângulo!')
    if segmento1==segmento2==segmento3:
        print('E é um TRIÂNGULO EQUILÁTERO')
    if segmento1==segmento2!=segmento3 or segmento1==segmento3!=segmento2 or segmento3==segmento2!=segmento1:
        print('E é um TRIÂNGULO ISÓCELES')
    if segmento1!=segmento2!=segmento3:
        print('E é um TRIÂNGULO ESCLENO')
else:
    print('Esses segmentos NÃO forma um triângulo!')