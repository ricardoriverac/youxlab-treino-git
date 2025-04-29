matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        valor = int(input(f'Digite um valor para a posição {i,j}'))
        matriz[i][j] = valor
        
for a in range(0,3):
    print(matriz[a])