def criar_matriz(n_linhas, n_colunas):
    matriz_resultado = [] 
    linha = []  

    while len(matriz_resultado) < n_linhas:
        try:
            numero = int(input('Insira um número: '))
            linha.append(numero)

            if len(linha) == n_colunas:
                matriz_resultado.append(linha)
                linha = []
        except ValueError:
            print("Por favor, insira um número válido.")
    
    return matriz_resultado

matrizlegal = criar_matriz(3, 3)
print("\nMatriz resultante:")
for linha in matrizlegal:
    print(linha)

soma_pares = sum(num for linha in matrizlegal for num in linha if num % 2 == 0)
soma_terceira_coluna = sum(linha[2] for linha in matrizlegal)
maior_segunda_linha = max(matrizlegal[1])

print(f"\nA) Soma de todos os valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")