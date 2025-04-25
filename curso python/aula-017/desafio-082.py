lista = []
listaPar = []
lista2 = []
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    par = num % 2
    if par == 0:
        listaPar.append(num)
        lista.append(num)
    if par == 1:
        lista2.append(num)
        lista.append(num)
print(f'A lista foi {lista}')        
print(f'Os números pares foram {listaPar}')
print(f'Os números impares foram {lista2}')