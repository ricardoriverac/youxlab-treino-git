numeros = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    numeros.append(valor)
maior = max(numeros)
menor = min(numeros)
print(f"\nVocê digitou os valores: {numeros}")
print(f"O maior valor foi {maior} nas posições: ", end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(i, end=' ')
print(f"\nO menor valor foi {menor} nas posições: ", end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(i, end=' ')
