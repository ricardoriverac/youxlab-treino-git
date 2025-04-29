a = int(input('Primeiro Valor: '))

b = int(input('Segundo Valor '))

c = int(input('Tercero Valor:'))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
  menor = c     

  print('O menor número digitado foi {}'.format(menor))
  
