palavras = ('Cadeia', 'Braço', 'Palavras', 'Obelisco', 'Braço', 'Alpiste', 'Supermercado', 'Casca', 'Alma',

            'Encerramento')

vowels = ('a', 'e', 'i', 'o', 'u')



for i in range(0, len(palavras)):

    numero_vogais = None

    vogais_exibir = ''



    for letras in palavras[i]:  



        for v in range(0, len(vowels)):  

            if vowels[v] == letras or vowels[v].upper() == letras:

                vogais_exibir += vowels[v]

                vogais_exibir += ' '



                if numero_vogais is None:

                    numero_vogais = 1

                else:

                    numero_vogais += 1



    print(f'\033[5:35mNa palavra \033[5:32m{palavras[i]} \033[5:35mhá um total de: \033[5:32m{numero_vogais} \033['

          f'5:35mvogais.\nAs vogais encontradas nessa palavra foram: \033[5:32m'

          f'{vogais_exibir.strip().replace(" ", ", ")}\033[5:35m.\n')