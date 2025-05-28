pessoa = {}
pessoas = []
soma_idade = 0
while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ").strip()
    while True:
        pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print("Erro! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    soma_idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
media_idade = soma_idade / len(pessoas)
print("RESULTADOS:")
print(f"- Total de pessoas cadastradas: {len(pessoas)}")
print(f"- Média de idade: {media_idade:.2f} anos")
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
print(f"- Mulheres cadastradas: {', '.join(mulheres) if mulheres else 'Nenhuma'}")
print(f"- Pessoas com idade acima da média:")
for p in pessoas:
    if p['idade'] > media_idade:
        print(f"  {p['nome']} - {p['idade']} anos")