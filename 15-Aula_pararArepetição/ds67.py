while True:
    n =int(input('Digite um numero: '))
    print('~'*10)
    if n<0:
        break
    for c in range(1 , 10):
        print(f'{n}x{c}={n*c}')
    print('~'*10)
print('Fim')