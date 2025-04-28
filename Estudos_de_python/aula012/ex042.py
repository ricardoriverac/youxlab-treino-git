
l1=int(input('Me diga o tamanho do lado 1: '))
l2=int(input('Me diga o tamanho do ladoc 2: '))
l3=int(input('Me diga o tamanho do lado 3: '))
print('<=>'*20)

if l1 ==l2 and l2 ==l3 and l3 ==l1:
    print('Triângulo Equilatero') 
elif l1 == l2 or l2 ==l3 or l3 ==l1:
    print('Triângulo Isósceles ')
else:
    print('Triângulo Escaleno')