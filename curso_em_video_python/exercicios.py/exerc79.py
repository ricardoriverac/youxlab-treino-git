numeros = []

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso.')
    else:
        print('Número repetido não será adicionado.')

    while True:
        resposta = input('Quer continuar? [S/N] ').strip().upper()
        if resposta in 'SN':
            break  
        print('Ocorreu um erro, digite de novo.')

    if resposta == 'N':
        print('FINALIZANDO...')
        break  
print('-' * 40)
ordemCrescente = sorted(numeros)
print(f'A lista ficou: {ordemCrescente}')