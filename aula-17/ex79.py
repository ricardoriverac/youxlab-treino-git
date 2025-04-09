num = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Digite outro número. ')
    r = str(input('Deseja continuar? '))
    if r in 'Nn':
        break
num.sort()
print('--'*35)
print(f'Você digitou os valores: {num}')