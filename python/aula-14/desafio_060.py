print('Vejamos o resultado de números fatoriais')

num = int(input('Digite um número: '))
resultado1 = num
resultado2 = 0

while num != 0:
    print(num, end='x')
    num -= 1
    if num == resultado1 - 1:
       resultado2 += resultado1 * num
    if num < resultado1 -1:
        resultado2 *= num
    if num == 1:
        num = 0
if resultado2 != 0:
    print(f'={resultado2}')
if resultado2 == 0:
    print('1 = 1')