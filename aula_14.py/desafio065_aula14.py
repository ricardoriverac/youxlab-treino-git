inserir = 'S'
soma = contador = maior = menor = 0
while inserir == 'S':
    número = int(input('Insira um número: '))
    if maior == 0 and menor == 0:
        maior = menor = número
    if número > maior:
        maior = número
    if número < menor:
        menor = número
    contador += 1
    soma += número
    inserir = input('Deseja inserir mais números? [S/N]: ').upper().strip()
média = soma / contador
print('Você inseriu {} números. A média deles é {:.2f}.'.format(contador, média))
print('O maior número inserido foi {} e o menor foi {}.'.format(maior, menor))