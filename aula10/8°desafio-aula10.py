#verificando se forma ou não um triângulo
segmento1=float(input('Digite o valor do primeiro segmento:'))
segmento2=float(input('Digite o valor do segundo segmento:'))
segmento3=float(input('Digite o valor do terceiro segmento:'))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Esses segmentos formam um triângulo!')
else:
    print('Esses segmentos NÃO forma um triângulo!')