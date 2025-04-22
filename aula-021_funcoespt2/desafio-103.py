def ficha(nome = '', gols=0):
    if nome == False:
        return print(f'Jogador <desconhecido>')


nome = str(input("Digite o nome do jogador: "))
gols = int(input(f"Número de gols de {nome}"))
print(f'O jogador ')