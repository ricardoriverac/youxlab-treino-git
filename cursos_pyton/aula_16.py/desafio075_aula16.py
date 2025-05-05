primNumero = int(input("Digite o primeiro número: "))
segNumero = int(input("Digite o segundo número: "))
tercNumero = int(input("Digite o terceiro número: "))
quartNumero = int(input("Digite o quarto número: "))
tupla = (primNumero, segNumero, tercNumero, quartNumero)


print(tupla)
count = 0
countPosicao = 0
countNum = 0
valorespares = []



for t in tupla:
    if t == 3:
        countPosicao = count
    if t % 2 == 0:
        valorespares.append(t)
    if t == 9:
        countNum+= 1
    count+= 1

print(f' O número 9 é encontrado {countNum}')
print(f'Os números pares são {valorespares}')
print(f'O número 3 foi digitado na posição {count}')





    



