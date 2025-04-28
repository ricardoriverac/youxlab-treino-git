matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(3):
    for c in range(3):
        numero = int(input('Digite um valor: '))
        matriz[l][c] = numero

print('-=' * 20)
for o in range(3):
    print(matriz[o])