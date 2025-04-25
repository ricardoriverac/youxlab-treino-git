brasileirao = ['Internacional', 'Corinthians', 'Ceará SC', 'Fortaleza', 'Botafogo', 
               'Flamengo', 'Palmeiras', 'Juventude', 'Fluminense', 'Grêmio', 'Vasco', 
               'Cruzeiro', 'Bahia', 'São Paulo', 'Bragantino', 'Santos', 'Mirassol', 'Sport Recife', 
               'Atlético-MG', 'EC vitória']
clubes_albafeto = [
    'Atlético-MG',
    'Bahia',
    'Botafogo',
    'Bragantino',
    'Ceará SC',
    'Corinthians',
    'Cruzeiro',
    'EC vitória',
    'Flamengo',
    'Fluminense',
    'Fortaleza',
    'Grêmio',
    'Internacional',
    'Juventude',
    'Mirassol',
    'Palmeiras',
    'São Paulo',
    'Santos',
    'Sport Recife',
    'Vasco'
]

escolha = str(input("Você quer ver informaçôes sobre o brasileirão? \033[33m[S/N]:\033[m ")).upper()
while escolha == 'S':
    
        
    posicao = brasileirao.index('Bragantino')
    print(f'\n Os 5 primeiro colocados são: {brasileirao[:5]}')

    print(f'\n Os 4 Ultimos colocados são: {brasileirao[16:]}')

    print(f'\n Os clubes em ordem alfabética: {clubes_albafeto}')

    print(f'\n O Bragantino esta na posição: {posicao}')

    if escolha =='N':
        break
print('-=' * 30)
print('OBRIGADO, VOLTE SEMPRE')
print('-=' * 30)



