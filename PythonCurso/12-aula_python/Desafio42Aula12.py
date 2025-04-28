
print('Analizador de ângulos')
 
r1 = float(input('Digite o valor da primeira reta '))
r2 = float(input('Digite o valor da segunda reta '))
r3 = float(input('Digite o valor da terceira reta'))
 
if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 +r2:
     print('Os segmentos acima podem formar um triângulo!!')

     if r1 == r2 == r3:
        print('Seu triângulo tem todos os lados iguais ele é Equilátero:')

     if r1 != r2 !=r3:
        print('Seu triângulo tem dois lados iguais ele é ISOSCALES')
     
     else:
        print('Escaleno')
else:
    print('Não pode formar um triângulo')
     


    
 

