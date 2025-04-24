def ficha():
    dados = dict()
    dados['nome'] = str(input('\033[3;34mNome do jogador: \033[m'))
    dados['gols'] = int(input(f'\033[3;34mQuantos gols {dados["nome"]} fez?\033[m '))
    print('-' * 30)
    n = len(dados["nome"])
    print(f'\033[1;34m{"NOME":<10}\033[1;36m {"GOLS":>10}\033[m')
    print('-' * 30)
    print(f'\033[3;34m{dados["nome"]:<10}{dados["gols"]:>10}\033[m')
    print('-' * 30)
    
enfeite = "-" * 30
print(f'{enfeite} \033[1;34mDADOS DO JOGADOR DO CRUZEIRO\033[m {enfeite}')

print('\033[1;34mDADOS\033[m')
ficha()
