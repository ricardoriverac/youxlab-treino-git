valores = []
for c in range(1, 6):
    numero = int(input(f"Digite o {c}° número: "))
    valores.append(numero)
maior = max(valores)
menor = min(valores)
pos_maior = []
pos_menor = []
for c in range(5):
    if valores[c] == maior:
        pos_maior.append(c + 1)
    if valores[c] == menor:
        pos_menor.append(c + 1)   
print(f"Os números digitados foram: {valores}")
print(f"O maior número digitado foi: {maior}, nas posições {pos_maior}")
print(f"O menor número digitado foi: {menor}, nas posições {pos_menor}")