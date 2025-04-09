lista = [] 
listaimpar = []
listapar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    sn = str(input('Deseja continuar [S/N]')).upper().strip()
    if sn == 'N':
        break
print(f'Lista: {lista}')
print(f'Números pares: {listapar}')
print(f'Números ímpares: {listaimpar}')