dados = [[]]

while True:
    nome = input('Nome: ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))

    pergunta = input('Quer continuar? [S/N] ').upper()

    if pergunta == 'N':
        break