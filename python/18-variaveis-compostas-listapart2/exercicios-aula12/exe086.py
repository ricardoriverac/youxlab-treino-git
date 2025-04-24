matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0
somadaterceiracoluna = 0
maiordalinha = 0
for l in range(3):
    for c in range(3):
        numero = int(input(f'Digite o valor para a [{[l]}, {[c]}]: '))
        matriz[l] [c] = numero
        if numero % 2 == 0 :
            pares += numero
        if c == 2 :
            somadaterceiracoluna += numero
        # solucao do jander
        if l == 1 :
            if numero > maiordalinha :
                maiordalinha = numero
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]' , end='')
    print()
print('-='*30)
print(f'A soma de todos os pares foi {pares}')
print(f'A soma dos pares foi {somadaterceiracoluna}')
print(f'O maior da segunda linha foi {maiordalinha}')
# solucao rodrigao
matriz_2 = matriz[1]
print(f'O maior da segunda linha foi :{max(matriz_2)}')



    