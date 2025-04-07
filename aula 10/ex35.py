print ("Analisador de triângulos!!")
lado1 = (input ("Primeiro segmento: "))
lado2 =  (input ("Segundo segmento: "))
lado3 =  (input ("Terceiro segmento: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print ("esses segmentos podem criar um triângulo!!!!")
else:
    print ("Não pode criar um triângulo!")