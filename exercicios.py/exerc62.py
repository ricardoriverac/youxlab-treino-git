a1 = int(input('Digite o primeiro termo da PA: '))
d = int(input('Qual é a razão da PA? '))

termo = a1
contador = 1
total = 0
mais = 10

while mais !=0:
    total += mais
    while contador <= total:
        print('{},'.format(termo), end='')
        termo += d
        contador += 1
    mais = int(input('Quer ver quantos termos a mais? '))
print('FINALIZADO.')
  