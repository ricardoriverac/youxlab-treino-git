ficha = []
while True:
    nome = str(input('Nome: '))

    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2)/2

    ficha.append ([nome,[nota1,nota2],media])

    resposta =str(input('Quer continuar [S/N] ').upper())

    if resposta == 'N':
        break

print(ficha)

print(f'{"Boletim :<4"}{"Nome":<10}{"Media":>8}')
print('-'*20)

for index , aluno in enumerate(ficha):
    print(f'{index:<4}{aluno[0]:<10}{aluno[2]:>8}')

while True:
    indexAluno = int(input('Quer saber a nota de qual aluno: (999 interrompe)'))
    if indexAluno == 999:
        break

    if indexAluno <= len(ficha) - 1:
        print(f'Notas de {ficha[indexAluno][0]} são {ficha[indexAluno][1]}')
        
