try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except:
    print('Algo deu errado.')
else:
    (f'O resultado da divisão é {r}')
finally:
    print(':)')