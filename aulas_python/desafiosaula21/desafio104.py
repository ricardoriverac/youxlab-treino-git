def leiaInt(msg):
    valido = False
    if not valido:
        numero = input(msg)
        if numero.isalpha():
            print(f'\033[31mERRO! \"{numero}\" é um preço inválido!\033[m ')
        else:
            valido = True
            return float(numero)

n = leiaInt('Digite um número: ')
print(f'O valor digitado foi {n} ')