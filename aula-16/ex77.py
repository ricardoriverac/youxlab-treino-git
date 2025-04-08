palavras = ('Cachorro', 'Gato', 'Passaro', 'Vaca', 'Boi', 'Porco', 'Cabra', 'Ovelha')
for p in palavras:
    print(f'\n Na palavra {p.upper()}, temos: ',end='')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais.lower(), end = ' ')