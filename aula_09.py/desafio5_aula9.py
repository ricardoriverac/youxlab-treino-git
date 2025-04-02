frase = str(input('Digite uma frase: '))
print('A letra A aparece {} vezes '.format(frase.upper().count('A')))
print('A letra A aparece na posição {} '.format(frase.find('a') +1))
print('A ultima posição que a letra A aparece é {}'.format(frase.rfind('a')+1))