continuacao = "S"
media = 0
boletim = list ()
while continuacao == "S":
    nome = str (input('Digite o nome do aluno: '))
    primeiraNota = int(input('Digite a primeira nota: '))
    segundaNota = int(input('Digite a segunda nota: '))
    media = (primeiraNota + segundaNota) / 2
    boletim.append([nome, [primeiraNota, segundaNota], media])
    continuacao = str (input ("Quer continuar [S/N] ? ")).strip().upper()
print('-=' * 20)
print(f'{"no.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 20)
for indice, aluno in enumerate(boletim):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    opcao = int(input("Mostrar notas de qual aluno? (999 para parar): "))
    if opcao == 999:
        break
    if 0 <= opcao < len(boletim):
        print(f'Notas de {boletim[opcao][0]} são: {boletim[opcao][1]}')
    else:
        print("Aluno não encontrado.")

