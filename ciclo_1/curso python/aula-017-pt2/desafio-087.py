matriz = []
for c in range(3):
    linhas = []
    for i in range (3):
        num = int(input('Digite um valor: '))
        linhas.append(num)
    matriz.append(linhas)
for l in matriz:
    print(l)

soma = 0
pares = 0
for l in matriz:
    for numero in l:
        if numero % 2 == 0:
            pares += numero
        soma += numero

outroNumero = 0
ultimosNums = []
segundaColu = []
for li in matriz:
    ultimosNums.append(li[2])
    segundaColu.append(li[1])
somaTerceira = sum(ultimosNums)
somaSegunda = sum(segundaColu)
print('-=' *30)
print(f'Os numeros das terceira coluna é {somaTerceira}')
print(f'A soma dos numeros da segunda coluna é {somaSegunda}')
print(f'A soma dos números é {soma}')
print(f'A soma dos números pares é {pares}')
print('-=' *30)


    #divisao = l % 2

# # Criando uma matriz 3x3 vazia
# matriz = []

# print("Digite os 9 elementos da matriz 3x3:")

# # Loop para preencher a matriz
# for i in range(3):
#     linha = []
#     for j in range(3):
#         elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
#         linha.append(elemento)
#     matriz.append(linha)



# Criando uma matriz 3x3 vazia
# matriz = []

# print("Digite os 9 elementos da matriz 3x3:")

# # Loop para preencher a matriz
# for i in range(3):
#     linha = []
#     for j in range(3):
#         elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
#         linha.append(elemento)
#     matriz.append(linha)

# # Mostrando a matriz formatada
# print("\nMatriz 3x3:")
# for linha in matriz:
#     print(linha)

# # Calculando a soma total e a soma dos pares
# soma_total = 0
# soma_pares = 0

# for linha in matriz:
#     for numero in linha:
#         soma_total += numero
#         if numero % 2 == 0:
#             soma_pares += numero

# print(f"\nSoma de todos os elementos da matriz: {soma_total}")
# print(f"Soma de todos os números pares da matriz: {soma_pares}")



