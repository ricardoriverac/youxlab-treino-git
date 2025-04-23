lista = []
impar= []
pares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    perg = ' '
    while perg not in 'SN':
        perg = str(input("\033[35;5;213mDeseja continuar? [S/N]'/033[0m")).upper()
    if perg in 'N':
        break
print(f'A lista completa é {lista}.')
for pos, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impar}.')