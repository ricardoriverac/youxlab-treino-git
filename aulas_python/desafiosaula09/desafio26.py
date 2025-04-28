frase = input('Digite uma frase: ').upper().strip()
#a = frase.count('a')
#A = frase.count('A')
#aA = a + A
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))