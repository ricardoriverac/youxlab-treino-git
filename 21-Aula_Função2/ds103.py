
def ficha():
    nome = input('Nome do jogador: ')
    gols = int(input('Total de gols na carreira: '))
    campeonato = input('Campeonato principal que joga: ')
    return [nome, gols, campeonato]


jogadores = [
    ["Neymar", 430, "Champions League"],
    ["Cristiano", 850, "Premier League"],
    ["Messi", 820, "La Liga"]
]


cabecalhos = ["Nome", "Gols", "Campeonato"]
larguras = [15, 6, 20]

def imprimir_linha(linha):
    print(f"{linha[0]:<{larguras[0]}} | {linha[1]:<{larguras[1]}} | {linha[2]:<{larguras[2]}}")


def imprimir_separador():
    print("-" * (sum(larguras) + 6))

def exibir_tabela():
    imprimir_separador()
    imprimir_linha(cabecalhos)
    imprimir_separador()
    for jogador in jogadores:
        imprimir_linha(jogador)
    imprimir_separador()


exibir_tabela()


novo = ficha()
jogadores.append(novo)


print("\nTabela atualizada:\n")
exibir_tabela()
