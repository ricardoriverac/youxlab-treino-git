#Aprimore o desafio anterior, mostrando no final:
#A soma de todos os valores pares digitados.
#A soma dos valores da terceira coluna
#O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
numPares = []
somaNumPar = 0
somaTerCo = 0
maiorValSegLin = 0

for l in range(3):
    for c in range(3):
        valor = int(input(f"Digite um valor para [{l}, {c}]: "))
        matriz[l][c] = valor

        if valor % 2 == 0:
            numPares.append(valor)
            somaNumPar += valor

for l in range(3):
    somaTerCo += matriz[l][2]

maiorValSegLin = max(matriz[1])

print("\n")
print("-=" * 11)
print("Matriz 3x3")
print("-=" * 11)

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

print(f"\nTodos os números: {matriz}")
print(f"Todos os números pares: {numPares}")
print(f"Soma dos números pares: {somaNumPar}")
print(f"Soma da terceira coluna: {somaTerCo}")
print(f"Maior valor da segunda linha: {maiorValSegLin}\n")
