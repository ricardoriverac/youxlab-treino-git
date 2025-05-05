#VOGAIS EM TUPLAS
palavras=('Gato','Cachorro','Zebra','Papagaio','Cobra',)
for palavra in palavras:
    print(f'\n{palavra} tem as vogais: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')