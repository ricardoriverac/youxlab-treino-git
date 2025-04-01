seg1 = int(input('Primeiro segmento? '))
seg2 = int(input('Segundo segmento? '))
seg3 = int(input('Terceiro segmento? '))

if seg1!=seg2 and seg1!=seg3 and seg2!=seg3:
    print('Esses segmentos formam um triângulo Escaleno')
    
elif seg1==seg2==seg3:
    print('Esses segmentos formam um triângulo Equiláterio')

elif seg1==seg2 or seg1==seg3 or seg2==seg3:
    print('Esses segmentos formam um triângulo Isósceles')
    
