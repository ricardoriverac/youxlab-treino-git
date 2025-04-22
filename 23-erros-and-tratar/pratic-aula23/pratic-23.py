try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O valor é {r}')
finally:
    print('Volte sempre!')