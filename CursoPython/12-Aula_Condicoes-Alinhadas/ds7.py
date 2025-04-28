n1=float(input('Primeiro '))
n2=float(input('Segundo '))
n3=float(input('Terceiro '))
if n1 < n2 + n3 and  n2 < n1 + n3 and n3 < n1 +n2:
    print('Podem formar um triangulo', end ='')
    if n1 == n2 == n3:
        print('Equilatero')
    if n1 != n2 !=n3 !=n1:
        print('Escaleno')
    else:
        print('isosceles')
else:
    print('Não e possivel formar triangulo')        
