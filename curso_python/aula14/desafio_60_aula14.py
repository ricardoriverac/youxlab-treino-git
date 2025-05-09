### While ###
from math import factorial
numero = int(input('Digite um número para calcular o seu fatorial: '))

comecoFatorial = numero
fatorial = 1

while comecoFatorial > 0:
    print (f'{comecoFatorial}' ,end='')
    if comecoFatorial > 1:
        print (' x ', end='')
    else:
        print (' = ', end='')

# ou apenas
# print (' x ' if comecoFatorial > 1 else ' = ' ,end='')

    fatorial *= comecoFatorial #ou fatorial = fatorial * comecoFatorial
    comecoFatorial -= 1 #ou comecoFatorial = comecoFatorial -1

print (fatorial)