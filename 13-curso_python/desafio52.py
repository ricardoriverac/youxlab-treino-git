numero = int(input('Digite um número: '))
isPrimo = True
for n in range(1, numero + 1):
    resto = numero%n
    if resto ==0:
        if numero!=n and n!=1:
          isPrimo = False 
          print('O nùmero {} NÃO É PRIMO.'.format(numero))
          break
if isPrimo == True :
   print('O número {} é primo. '.format(numero))
       