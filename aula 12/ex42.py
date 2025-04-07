print ("Analisador de triângulos!!")
lado1 = (input ("Primeiro segmento: "))
lado2 =  (input ("Segundo segmento: "))
lado3 =  (input ("Terceiro segmento: "))
if lado1 == lado2 == lado3: 
    print ("Triângulo EQUILÁTERO!!!!")
elif lado1 != lado2 == lado3 or  lado2 != lado3 == lado1 or lado3 != lado2 == lado1:
    print ("Triângulo ISÓSCELES!!!!")
else:
    print ("Triângulo ESCALENO!!!!")

