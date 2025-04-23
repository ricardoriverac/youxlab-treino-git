lista=[]
dados=[]
maior = 0
menor = 0
while True:
    dados.append(str(input("\033[38;5;213mNome:\033[0m ")).title().strip())
    dados.append(float(input("\033[35;5;213mPeso:\033[0m" )))
    if len(lista) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    r = str(input('deseja continuar? [S/N]')).upper()
    if r in 'N':
        break
print(f'ao todo vc cadastrou {len(lista)} pessoas.')
print(f'Maior peso foi {maior} . Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'Menor peso foi {menor}. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(p[0], end=' ')
