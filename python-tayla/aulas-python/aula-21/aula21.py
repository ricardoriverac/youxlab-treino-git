# testando o return
def fatorial(numero = 1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f

#fazendo com mais de uma variável
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os valores são {f1} {f2} e {f3}')

#fazendo com uma variável só
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

# vendo return false ou true
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input('Digite um número: '))
print(par(numero)) # desse jeito só mostra False ou True

if par(numero): # esse jeito mostra a mensagem bonitinha
    print('É par!')
else:
    print('Não é par!')