# Crie um dicionario com alunos e suas notas, calcule a média de cada aluno.

# resultado experado:
# Ana: 8.0
# Lucas: 5.22
# Joao: 7.1

# alunos = {
#     'Ana': [7, 8, 9],
#     'Bruno': [5, 6, 5],
#     'Clara': [10, 9, 10, 7]
# }

# for nome, notas in alunos.items(): # nome, notas. em alunos.items() = retorna todos valores da lista
#     media = sum(notas) / len(notas) #media = sum(soma) / len(tamanho)notas
#     print(f'{nome}: {media:.2f}')

alunos = {}

while True:
    nome = input("Digite um nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    alunos[nome] = [nota1, nota2, nota3, nota4]
    pergunta = input("Deseja continuar cadastrando? [S/N] ").strip().upper()

    if pergunta not in ["S", "N"]:
        print("\nResposta inválida.\n")
        break

    if pergunta == "N":
        print("\nPrograma encerrado.\n")
        break

for nome, notas in alunos.items(): # nome, notas. em alunos.items() = retorna todos valores da lista
    media = sum(notas) / len(notas) #media = sum(soma) / len(tamanho)notas
    situacao = True
    if situacao:
        if media >= 7:
            print("Situação ")
    print(f'{nome}: {media:.2f}: {situacao}')