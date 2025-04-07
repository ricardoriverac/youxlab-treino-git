numero = int(input('Digite um número: '))
isPrimo = True
for c in range(1, numero+1):
    resto = numero%c
    if resto==0:
        if numero!=c and c!=1:
            isPrimo = False
            print('Esse número {}NÃO É PRIMO{} '.format('\033[35m', '\033[m'))
            break
if isPrimo==True:
    print('O número {} é {}PRIMO{}'.format(numero, '\033[35m', '\033[m'))
    

     
            
        