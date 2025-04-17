valores = []
for c in range (5):
    numero = int (input(f"Digite o { c + 1}º número : "))
    posicao = 0
    while posicao < len(valores) and valores[posicao] < numero:
        posicao += 1
    valores.insert(posicao, numero)
    print (f"O número foi \033[34m{numero}\033[m foi inserido na posição {posicao + 1}.")
print (f" A lista ordenada é: \033[32m{valores}\033[m")