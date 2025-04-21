ficha = list()
while True:
    nome = str(input('Qual o nome: '))
    nota1 = float(input('Nota 1 '))
    nota2 = float(input('Nota 2 '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    responda = str(input('Quer continuar?? [S/N]'))
    if responda in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' *35)
    opçao = int(input('Mostar notas de qual aluno? para finalizar digite 999 !!'))
    if opçao == 999:
        print('FINALIZANDOOOO')
        break
    if opçao <= len(ficha) - 1:
        print(f'Notas de {ficha[opçao][0]} são {ficha[opçao][1]}')
print('Espero que tenha Gostado Zé')
    
