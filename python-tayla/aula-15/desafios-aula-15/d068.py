from random import randint

print('\033[1m=-\033[m' * 17)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('\033[1m=-\033[m' * 17)

numero = 0
computador = randint(1, 10)
soma = 0

while True:
    numero = int(input('Digite um valor: '))
    pergunta = input('Par ou Ímpar? [P/I] ').upper().strip()

    if (numero + computador) % 2 == 0:

        print('\033[1m-\033[m' * 34)
        print(f'Você jogou {numero} e o computador {computador}. Total de {numero + computador} DEU PAR')
        print('\033[1m-\033[m' * 34)

        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('\033[1m=-\033[m' * 17)
        soma += 1
    else:
        print('\033[1m-\033[m' * 34)
        print(f'Você jogou {numero} e o computador {computador}. Total de {numero + computador} DEU ÍMPAR')
        print('\033[1m-\033[m' * 34)

        print('Você PERDEU!')
        print('\033[1m=-\033[m' * 17)
        print(f'GAMER OVER! Você venceu {soma} vezes')
        break