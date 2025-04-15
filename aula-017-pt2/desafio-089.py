isRodando = True
boletim = []
alunos = []
notaAlunos = []
def boletim_escolar():
    while isRodando:
        nome = str(input("Digite um nome: "))
        alunos.append(nome)
        nota = float(input(f"Digite a 1a nota de {nome}: "))
        nota2 = float(input(f"Digite a 2a nota de {nome}: "))
        soma = nota + nota2
        media = soma / 2
        alunos.append(media)
        continuar = str(input("Quer continuar? S/N: ")).upper()
        if continuar == "S":
            continue
        else:
            for aluno in alunos:
                print(aluno)
            break
    print(f'A Média desses alunos é {media}')

boletim_escolar()

