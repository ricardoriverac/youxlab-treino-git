lista = ('Ana Clara', 'Maria Luiza', 'Marianne' ,'Anna Luiza', 'Joao Pedro', 'Keverson', 'Garcia', 'Yuri', 'Davi', 'Gustavo', 'Alice', 'Thaila', 'Geovanna', 'Vinícius', 'Julio')
for vogais in lista:
    print(f'\nNo nome \033[1;35m{vogais}\033[m tem: ', end='')
    for letra in vogais:
        if letra in 'AaEeIiOoUu':
            print(f'\033[1;31m{letra}\033[m', end=' ')