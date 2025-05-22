soma = 0
cont = 0
print('Digite numeros: "999 para parar"')

while True:
    numero = int(input("Numero: "))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'A soma entre os {cont} numero(s) vale {soma}')