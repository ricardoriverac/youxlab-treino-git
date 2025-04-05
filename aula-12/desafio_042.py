print('-='*30)

print('   Analisador de triângulos v. 2.0      ')

print('-='*30)

l1=float(input('Digite a medida do lado 1: '))

l2=float(input('Digite a medida do lado 2: '))

l3=float(input('Digite a medida do lado 3: '))

if  (l1+l2)<=l3 or (l2+l3)<=l1 or (l1+l3)<=l2:

    print('As medidas digitadas não podem formar um triângulo')

else:

    print('As medidas digitadas formam um triângulo')

if l1!=l2!=l3 and not ((l1+l2)<=l3 or (l2+l3)<=l1 or (l1+l3)<=l2):

    print('O triangulo é ESCALENO')

elif l1 == l2 ==l3:

    print('O triangulo é EQUILATERO')

elif l1==l2 and l1!=l3 or l1==l3 and l1!=l2 or l2==l3 and l2!=l1:

    print('O triangulo é ISOSCELES')