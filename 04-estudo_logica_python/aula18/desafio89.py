lista = []
while True:
    nome = str(input('Digite o nome: ')).title()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Digite a segunda nota:'))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    pergunta = str(input('Deseja continuar? (S/N): '))
    if pergunta in 'nN':
        break
print('--'* 40)   
print(f'{"N°":<4} {"NOME":<10}{"MÉDIA":>8}')
for i, n in enumerate(lista):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8}')

while True:
    print('--'*40)
    escolha = input('Você ver a nota de qual aluno? (digite "sair" para encerrar): ').strip().lower()
    if escolha == 'sair':
        print('\nSistema encerrado!!')
        break
    if escolha.isdigit() and int(escolha) < len(lista):
        escolha = int(escolha)
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')
    else:
        print(' Tente novamente.')
