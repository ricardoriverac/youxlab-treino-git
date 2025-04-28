a1 = int(input('Digite o primeiro termo da PA: '))
d = int(input('Qual é a razão da PA? '))
termo = a1
contador = 1
while contador <= 10:
    print('{},'.format(termo), end='')
    termo = termo + d
    contador += 1

