numero = int(input('Digite um número: '))
primo = numero%2
tot = 0
for n in range(1, numero +1):
    if numero % n ==0:
      print('\033[35m', end=' ')
      tot += 1
    else :
       print('\033[31m', end=' ')
    print('{}'.format(n), end = ' ')
print('O número {} foi divisível {} vezes.'.format(numero, tot)) 