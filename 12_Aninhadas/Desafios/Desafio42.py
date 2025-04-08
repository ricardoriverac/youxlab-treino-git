comprimento1= int(input("Insira um comprimento: "))
comprimento2= int(input("Insira outro comprimento: "))
comprimento3= int(input("Insira o terceiro comprimento "))
if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento1 + comprimento2:
    print("Os segmentos pode formar um triangulo")
    if comprimento1 == comprimento2 and comprimento2 == comprimento3:
        print("Equilatero")
    elif comprimento1 != comprimento2 != comprimento3 != comprimento1:
            print("Escaleno")
    else:
         print("Isosceles")
