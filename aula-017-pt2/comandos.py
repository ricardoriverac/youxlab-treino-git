# dados = ['Pedro', 'João']
# pessoas = [         ]
# pessoas.append(dados[:])
# print(pessoas[0])
# #lista.sort() oredena a lista de forma crescente
#lista.sort(reverse=True) lista de forma decrescente

import random

def gerar_jogos_megasena():
    print("=== Gerador de Palpites da Mega-Sena ===")
    qtd_jogos = int(input("Quantos jogos você quer gerar? "))

    todos_os_jogos = []

    for i in range(qtd_jogos):
        jogo = sorted(random.sample(range(1, 61), 6))
        todos_os_jogos.append(jogo)

    print("\n=== Seus Palpites ===")
    for i, jogo in enumerate(todos_os_jogos, start=1):
        print(f"Jogo {i}: {jogo}")

# Executar o programa
gerar_jogos_megasena()

