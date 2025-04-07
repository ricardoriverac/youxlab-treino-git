np = int(input('Digite um número para verificarmos: '))
contprimo = 0
for c in range (2,np+1):
    if np%c == 0:
        print(f'O número {np} é divisível por {c}.')
        contprimo += 1
    else:
        np%c == 1
        print(f'O número {np} não é divisível por {c}.')
if contprimo >= 2:
    print (f'O número {np} não é um número primo.')
else:
    print (f'O número {np} é um número primo.')