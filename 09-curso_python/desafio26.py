frase = input('Escreva uma frase: ').upper()
letraA = (frase.count('A'))
letraAM = (frase.count('a'))
letrasA = letraA + letraAM
print('Sua frase possui {} letras A'.format(letrasA))
print('A primeira letra A aparece na {} posição.'.format(frase.find('A')))
print('A última letra A aparece na {} posição.'.format(frase.rfind('A')))

