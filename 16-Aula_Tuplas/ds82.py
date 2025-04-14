
valores = []
pares = []
impares = []

quantidade = int(input("Quantos números você quer digitar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    valores.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('_'*20)
print("\nLista completa:", valores)
print("Números pares:", pares)
print("Números ímpares:", impares)
print('°' * 20)
