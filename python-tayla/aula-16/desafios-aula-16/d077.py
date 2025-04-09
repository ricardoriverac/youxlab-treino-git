palavra = ('jogar', 'programar', 'blusa', 'esporte', 'tinta', 
         'comida', 'desenho', 'carro', 'bicicleta', 'natal')
vogal = ('a', 'e', 'i', 'o', 'u')

for vogal in palavra:
    print(f'Na palavra {vogal} temos: ', end='')

    for letras in range(0, len(vogal)):
        if vogal[letras] == 'a' or vogal[letras] == 'e' or vogal[letras] == 'i' or vogal[letras] == 'o' or vogal[letras] == 'u':
            print(vogal[letras])