from time import sleep
while True:
    n =int(input('Digite um numero: '))
    print('~'*10)
    if n<0:
        break
    for c in range(1 , 10):
        sleep(1)
        print(f'{n}x{c}={n*c}')
        sleep(1)
    print('~'*10)
print('Fim')