n1=int(input('Primeiro numero: '))
n2=int(input('Segundo numero: '))
n3=int(input('Terceiro numero: '))
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n2 and n3<n1:
    menor=n3
maior=n1
if n2 > n1 and n2 > n3:
    maior=n2
if n3>n2 and n3>n1:
    maior=n3
print('O menor valor digitado foi {} '.format(menor))
print('O maior valor digitado foi {} '.format(maior))