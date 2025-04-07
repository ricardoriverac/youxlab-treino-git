from time import sleep
n = int(input('Digite 1 numero para o seu fatorial: '))
c = n
f = 1
print('Calculando sua fatorial.....{}! = '.format(n), end =' ')

while c  > 0:
    
    print('{}'.format(c), end = ' ')
    print(' x ' if  c >1  else '=', end = ' ')
    f *= c
    c -= 1
  
print('{}'.format(f))