def leiaint(msg):
    ok =False
    valor = 0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            valor= int(n)
            ok = True
        else:
            print('Erro Digite outro valor ')
        if ok:
            break
    return valor

n=leiaint('Digite um número: ')
print(f'O valor que você digitou foi {n}')

