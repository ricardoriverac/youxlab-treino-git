pessoas = []
mais_pesado = mais_leve = 0
while True:
    nome = input("Nome: ")
    peso = float(input("Peso (kg): "))
    pessoa = [nome, peso]
    pessoas.append(pessoa)
    if len(pessoas) == 1:
        mais_pesado = mais_leve = peso
    else:
        if peso > mais_pesado:
            mais_pesado = peso
        if peso < mais_leve:
            mais_leve = peso
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")
print(f"Pessoas com maior peso ({mais_pesado} kg): ", end="")
for p in pessoas:
    if p[1] == mais_pesado:
        print(f"[{p[0]}] ", end="")
print()
print(f"Pessoas com menor peso ({mais_leve} kg): ", end="")
for p in pessoas:
    if p[1] == mais_leve:
        print(f"[{p[0]}] ", end="")
print('finalizando o programa...')