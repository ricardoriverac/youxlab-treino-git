try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError ):
    print('Tivemos um problema com os dados que você digitou.')
except ZeroDivisionError:
    if a != 0:
        r = a
        print(f'O resultado é {r}')

    # print('Não é possível dividir um número por 0')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print(':) volte sempre')