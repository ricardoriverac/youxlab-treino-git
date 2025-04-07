print('Digite quantos números você quiser que te darei a soma deles. Para parar digite 999')
soma = 0

while True:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
    else:
        print('A soma de todos números foi {}'.format(soma))
        break