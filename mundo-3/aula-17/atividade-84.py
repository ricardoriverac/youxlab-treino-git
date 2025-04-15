pessoas = []
dados = []

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])  
    dados.clear()
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break


print(f"\nA) Total de pessoas cadastradas: {len(pessoas)}")

pesos = [p[1] for p in pessoas]
maior = max(pesos)
menor = min(pesos)

print(f"B) O maior peso foi {maior}kg. Peso de:", end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')
print()

print(f"C) O menor peso foi {menor}kg. Peso de:", end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')
print()
