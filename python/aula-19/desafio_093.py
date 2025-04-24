jogo = dict()
jogo['jogador'] = str(input('Nome do jogador: '))
jogo['jogos'] = int(input(f'Quantos jogos {jogo["jogador"]} jogou: '))

# Adicionando os gols de cada jogo
for c in range(0, jogo['jogos']):
    jogo[f'{c + 1}° Jogo'] = int(input('Número de gols: '))

print('-=' * 20)
print(jogo)
print('-=' * 20)

# Imprimindo os dados no formato adequado
for k, v in jogo.items():
    print(f'No campo {k}, tem o valor {v} jogos')

print('-=' * 20)

# Inicializando variáveis para contagem
cont = 0
contgols = 0

print(f'O jogador {jogo["jogador"]}, jogou {jogo["jogos"]} jogos;')
# Removendo as chaves 'jogador' e 'jogos' do dicionário
jogo.pop('jogador')
jogo.pop('jogos')

# Exibindo a quantidade de gols por jogo
for c in jogo.items():
    print(f'    ==> Na partida {cont + 1}, fez {c[1]} gols.')
    contgols += c[1]
    cont += 1
print(f'A soma de gols foi {contgols}.')
