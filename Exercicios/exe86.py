#Crie um programa que crie uma matriz de dimennsão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("\n")
print("-=" * 11)
print("Matriz 3x3")
print("-=" * 11)
for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()