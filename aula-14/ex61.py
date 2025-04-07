primter = int(input('Primeiro termo da razão PA: '))
razao = int(input('Razão da PA: '))

termo = primter
contador = 0

print('{}'.format(primter),end = ' ')

while contador < 10:
    pr = termo + razao
    print('{}'.format(pr), end = ' ')
    termo += razao
    contador += 1