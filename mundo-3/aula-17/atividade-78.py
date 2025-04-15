
valores = []


for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))
    valores.append(num)


maior = max(valores)
menor = min(valores)

posicoes_maior = [i for i, v in enumerate(valores) if v == maior]
posicoes_menor = [i for i, v in enumerate(valores) if v == menor]

print(f"\nVocê digitou os valores: {valores}")
print(f"O maior valor digitado foi {maior} nas posições {posicoes_maior}")
print(f"O menor valor digitado foi {menor} nas posições {posicoes_menor}")
