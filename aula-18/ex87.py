matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = par = impar = tc = somatc  =  0
for i in range(0,3):
    for j in range(0,3):
        valor = int(input(f'Digite um valor para a posição {i,j}'))
        matriz[i][j] = valor
        if valor % 2 == 0:
            soma += valor
        if j == 2:
            somatc += valor

for a in range(0,3):
    print(matriz[a])
print(f'A soma de todos valores pares é:{soma}')
print(f'A soma de todos valores da terceira coluna é igual a: {somatc}')
print(f'O maior valor da segunda linha é : {max(matriz[1])}')