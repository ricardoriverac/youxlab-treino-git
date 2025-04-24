numeros = []
pares = []
impares = []

while True:
    try:
        num = int(input("Digite um número (ou 'sair' para encerrar): "))
        numeros.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    except ValueError:

        print("Encerrando a entrada de números.")
        break

print("\nLista completa:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
