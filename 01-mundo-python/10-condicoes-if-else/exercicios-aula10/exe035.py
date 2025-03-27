s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 :
    print('Os segmentos \033[0;36mpodem formar\033[m um TRIÂNGULO ')
else:
    print('Os segmentos \033[0;31mNão Podem formar\033[m um TRIÃNGULO ')    