from time import sleep
medida1 = float(input('Digite três medidas para um triângulo: '))
medida2 = float(input(' '))
medida3 = float(input(' '))
print('Com essas medidas dá para formar um triângulo?') 
print('VERIFICANDO...')
sleep(2)
if medida1 < medida2 + medida3 and medida2 < medida1 + medida3 and medida3 < medida1 + medida2 :
    print ('Com essas medidas não dá para formar um triângulo.')
else :
    print ('Com essas medidas é possível formar um triângulo.')

if medida1 == medida2 == medida3 :
    print('Seu triângulo será Equilátero!')
elif medida1 == medida2 or medida2 == medida3 or medida1 == medida3 :
    print('Seu triângulo será Isóceles!')
else :
    print('Seu triângulo será Escaleno!')
