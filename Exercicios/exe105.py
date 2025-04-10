# Faça um programa que tenha uma função notas() que pode receber várias notas
# E vai retornar um dicionario com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)

# Adicione tambem as docstring

def notas(*numero, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    """

    registro = dict()
    registro["total"] = len(numero)
    registro["maior"] = max(numero)
    registro["menor"] = min(numero)
    registro["média"] = sum(numero) / len(numero)

    if situacao:
        if registro["média"] >= 7:
            registro["situação"] = "Boa"
        elif registro["média"] >= 5:
            registro["situação"] = "Razoavel"
        elif registro["média"] < 5:
            registro["situação"] = "Ruim"
    return registro

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
print("\nNotas cadastradas.\n")

resultado = notas(nota1, nota2, nota3, nota4, situacao=True)
print(resultado)