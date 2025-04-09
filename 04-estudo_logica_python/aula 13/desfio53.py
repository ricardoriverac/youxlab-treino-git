#frase=str(input(' Digite uma palavra :')).strip().upper().split()
#print('a palavra {} ao contrario é {} '.format(frase, frase[::-1]), end='')
#if frase == frase[::-1]:
 #   print(' É uma POLÍNDROMO'.format(frase))
#else:
 #   print('Nao é uma POLÍDROMO'.format(frase))    
frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso =''

for letra in range(len(junto) -1, -1, -1):
     inverso +=junto [letra]

if inverso == junto:
   print('Temos um palindrome!')

else:
     print('A frase digitada não é um palindrome!')