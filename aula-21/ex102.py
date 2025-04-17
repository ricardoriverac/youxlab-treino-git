import math

show = False
n = 0

num = int(input('Deseja fatorar qual número? '))
resp = str(input('Deseja mostrar o cálculo [s/n]? ')).lower()[0]

if resp == 's':
    show = True


def lin():
    print('--'*30)

def funcao(num,show=False):
    lin()


    fatorial = math.factorial(num)

    if show == True:
        for n in range(1, num+1):
            if num != 1:
                print(f'{num} x ',end='')
                num -= 1
            else:
                print(f'1 = ',end='')    



    print(f'{fatorial}', end = ' ')
    

funcao(num,show)
print()

