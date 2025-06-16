def leiaInt(num):
    if num.isnumeric():
        num = int(num)
    if isinstance(num, str):
        raise ValueError (f'o valor "{num}" não é válido, apenas valores inteiros')
    else:
        return print(f'Você digitou o valor {num}')



try:
   n = leiaInt(input('Digite um valor: '))

except ValueError as erro:
    print(f'Erro {erro}')