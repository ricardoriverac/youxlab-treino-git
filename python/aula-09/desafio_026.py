frase = str(input('Digite uma frase: ')).upper().strip()
print('Sua frase foi: {}!'.format(frase))
if 'A' in frase:
    print('Quantas vezes aparece a letra A na frase? {}'.format(frase.count('A')))
    print('A letra A aparece pela primeira vez na posição {}!'.format(frase.find('A')+1))
    print('A letra A aparece pela última vez na posição {}!'.format(frase.rfind('A')+1))
else:
    print('Não existe a letra A na sua frase!')