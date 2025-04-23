matriz = [[0, 0 ,0],[0, 0 ,0],[0 ,0 ,0]]
somaPar = 0
maiorValor = 0
somaColuna = 0
for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int (input (f'Digite um valor: {[linha], [coluna]}'))
print ('-=' * 30)
for linha in range (0,3):
    for coluna in range (0,3):
        print (f"[{matriz[linha][coluna]}]", end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print ()
print ('-=' * 30)
print (f"A soma dos valores pares é {somaPar}.")
for linha in range (0,3):
    somaColuna += matriz[linha][2]
print (f"A soma dos vetores da terceira coluna é {somaColuna}.")
for coluna in range (0,3):
    if coluna == 0:
        maior =  matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior =  matriz[1][coluna]
print (f"O maior valor da segunda linha é {maior}.")


