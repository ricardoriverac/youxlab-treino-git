a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
an = 0
termo = a1

print('\033[4mEsses são os 10 primeiros termos da PA:\033[m ')

while an < 10:
    print(termo, '->', end=' ')
    termo += r
    an += 1

print() #quebra de linha

print('-=' * 12)
maisTermos = (input('Quer saber mais termos da PA? [S/N] ',)).strip().upper()
if maisTermos == 'S':
    resposta = int(input('Quantos? '))
    an = 0
    while an < resposta:
        print(termo, '->', end=' ')
        termo += r
        an += 1
    print('Fim')
else:
    print('Fim')