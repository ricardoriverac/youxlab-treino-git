valores = []
for i in range(1, 6):
    numero = int(input(f"Digite o {i}° número: "))
    valores.append(numero)
maior = max(valores)
menor = min(valores)
posicaoMaior = valores.index(maior)
posicaoMenor = valores.index(menor)
print(f"Os números digitados foram: {valores}")
print(f"O maior número digitado foi: {maior}, na posição {posicaoMaior}")
print(f"O menor número digitado foi: {menor}, na posição {posicaoMenor}")