def soma(num, num2):
    soma = num + num2
    print(soma)
try:
    print('-=' *30)
    num = int(input('Digite um num: '))
    print('-=' *30)
    num2 = int(input('Digite outro num: '))
    print('-=' *30)

except (ValueError, TypeError):
    print(f'Problema nos tipos de dados que você digitou.')
except (ZeroDivisionError):
    print('Não pode ser divido por zero.')
except KeyboardInterrupt:
    print('O usuario preferiu não digitar valores')

else:
    print('-=' *30)
    print('Deu certo')
    soma(num, num2)
    print('-=' *30)
finally:
    print('Volte sempre!')

