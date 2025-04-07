while True:
    n = int(input('Digite o valor que você quer a tabuda: '))
    print('-='*20)
    if n < 0:
        break
    for c in range(1,11):
            a = c * n
            print(n,'X', c, '=', a)
            print('-'*30)
print('Finalizando...')