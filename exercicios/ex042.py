print('_='*20)
print('Analisador de Triângulos')
print('_='*20)
reta1= float(input('Primeiro segmento: '))
reta2= float(input('Segundo segmento: '))
reta3= int(input('Terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
    reta1 == reta2 and reta1 == reta3 and reta2 == reta1 and reta2 and reta3 and reta3 == reta1 and reta3 == reta2
    print('O triângulo é ISÓSCELES')

elif reta1 == reta2 == reta3 and reta2 == reta1 == reta3 and reta3 == reta1 == reta2:
    print('O triângulo é EQUILÁTERO')

elif reta1 != reta2 and reta2 != reta3 and reta1:
    print('O triângulo é ESCALENO') 
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO!')

