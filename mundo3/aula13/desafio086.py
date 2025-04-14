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
