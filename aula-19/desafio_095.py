dados = list()

jogadores = dict()



gols = list()

total_gols = 0



print('\033[1;97m-\033[m' * 35)

while True:

    jogadores['nome'] = str(input('Nome do jogador: '))

    jogadores['partidas jogadas'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))

    for c in range(0, jogadores['partidas jogadas']):

        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))

        total_gols += gols[c]

    jogadores['gols'] = gols.copy()

    gols.clear()

    jogadores['total'] = total_gols

    total_gols = 0

    dados.append(jogadores.copy())



    while True:

        print('\033[1;97m-\033[m' * 35)

        continuar = str(

            input('\033[;97mQuer continuar? [\033[;32mS\033[;97m/\033[;32mN\033[;97m]:\033[m ').strip().upper())

        print('\033[1;97m-\033[m' * 35)

        if continuar[0] in 'SN':

            break

        else:

            print(f'\033[;31mComando Inválido!\033[m')

    if continuar == 'N':

        break



print()

#print(dados)

print('\033[1;97m=\033[m'*40)

print(f'\033[1;30;107m {"Cod":<6}{"Nome":<12}{"Total":<9}{"Gols":}        \033[m')

print('\033[1;97m=\033[m'*40)

for c, jogadores in enumerate(dados):

    print(f'  {c:<4} {jogadores["nome"]:<13} {jogadores["total"]:<7} {jogadores["gols"]}')

print('\033[1;97m=\033[m'*40)

while True:

    from time import sleep

    print('\033[1;34m-\033[m' * 40)

    pergunta = int(input('\033[;97mMostrar dados de qual jogador? [Cod]:\033[m '))

    if pergunta == 999:

        print('\033[1;33msaindo...\033[m')

        sleep(1.5)

        break

    #Poderia colocar a tabela...

    print(f'\033[;97mO jogador \033[;32m{dados[pergunta]["nome"]}\033[;97m jogou \033[;32m{dados[pergunta]["partidas jogadas"]}\033[;97m partidas.\033[m')

    for k, v in enumerate(dados[pergunta]["gols"]):

        print(f'   \033[1;31m=> \033[;97mNa partida \033[;30m{k+1}\033[;97m, fez \033[;32m{v}\033[;97m gols.\033[m')

    print(f'\033[;97mFoi um total de \033[;32m{dados[pergunta]["total"]}\033[;97m gols.\033[m')

    print('\033[1;35m-\033[m' * 40)