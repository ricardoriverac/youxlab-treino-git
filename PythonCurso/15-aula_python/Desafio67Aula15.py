while True:
    print('-=-'*10)
    n = int(input('Quer ver a tabuda de qual valor? '))
    print('-=-'*10)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
print('='*30)
print('Obrigado por usar nosso programa!!')
print('-=-'*10)
