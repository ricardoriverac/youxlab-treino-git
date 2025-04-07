lista = []
for c in range(1, 7):
    num = int(input('{}º número: '.format(c)))
    if num % 2 == 0:
        lista.append(num)
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(' ')
print('A soma dos valores pares digitados foi: {}'.format(soma))