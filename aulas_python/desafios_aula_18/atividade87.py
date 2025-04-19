par = []
TerceiraColuna = []

matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] ')) 

print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()
        
    
par = [n for linha in matriz for n in linha if n % 2 == 0]
soma = sum(par)
print('-='*30,f'\nA soma dos números pares é: {soma}')

soma = (matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])
print(F'A soma dos números da terceira coluna é: {soma}')

maximo = max(matriz[1])
print(f'O maior número da segunda linha é: {maximo}')