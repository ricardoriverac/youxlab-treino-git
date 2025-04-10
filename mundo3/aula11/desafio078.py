valores = []
posicaomaior =[]
posicaomenor = []
for p in range(5):
    valores.append(int(input(f'digite o {p} número: ')))
maior = max(valores)
menor = min(valores)
for pos, v in enumerate(valores):
    if v == maior:
        posicaomaior.append(pos)
    if v == menor:
        posicaomenor.append(pos)
print(f'Você digitou os valores: {valores}.')
print(f'O maior valor digitado foi {maior} nas posições {posicaomaior}.')
print(f'O menor valor digitado foi {menor} nas posições {posicaomenor}.')

