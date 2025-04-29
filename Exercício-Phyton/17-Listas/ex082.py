numeros = []
pares = []
impares = []

while True:
    entrada = input("Digite um número (ou 'sair' para terminar): ")


    if entrada.lower() == 'sair':
        break
    
    numero = int(entrada)
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números Digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)