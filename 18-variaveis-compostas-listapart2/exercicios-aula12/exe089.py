pessoa = []
dados = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    pessoa.append(nome)
    pessoa.append(nota1)
    pessoa.append(nota2)
    dados.append(pessoa[:])
    pessoa.clear()
    sair = str(input('Quer continuar [S/N] ')).upper().strip()
    if sair == 'N' :
        break
for d in dados :
    media = (d[1] + d[2]) / 2 
print('No. Nome  Media') 
for p in range(len(dados)):
    print(f'[{p}] [{dados[p][0]}] [{media}]')
print('-='*20)
while True:
    numero = int(input('Mostra notas de qual alunos: [999  interromper]: '))
    for p in range(len(dados)):
        if numero == p :
            print(f'A nota do aluno escolhido foi {dados[p][1] , dados[p][2]}')