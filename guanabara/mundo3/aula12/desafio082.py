lista = []
par = []
impar = []
while True:
    numero = int(input('digite um numero:'))
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    escolha = str(input('deseja continuar? [S / N]:')).strip().lower()
    if escolha == 'n':
        break
print(f'''a lista completa é {lista}
os numeros pares são {par}
e os numeros impares são {impar}''')