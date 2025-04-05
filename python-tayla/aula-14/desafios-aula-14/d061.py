a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
an = 0
termo = a1
print('\033[4mEsses são os 10 primeiros termos da PA:\033[m ')
while an < 10:
    print(termo, '->', end=' ')
    termo += r
    an += 1