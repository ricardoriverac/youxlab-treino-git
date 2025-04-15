pessoas = []
soma_idades = 0

while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ").strip()
    
    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
        else:
            print("Erro! Por favor, digite apenas M ou F.")
    
    while True:
        try:
            idade = int(input("Idade: "))
            pessoa['idade'] = idade
            break
        except ValueError:
            print("Erro! Digite uma idade válida.")
    
    soma_idades += pessoa['idade']
    pessoas.append(pessoa.copy())
    
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)

print(f"A) Total de pessoas cadastradas: {len(pessoas)}")

media = soma_idades / len(pessoas)
print(f"B) A média de idade é de {media:.2f} anos.")

mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
print(f"C) As mulheres cadastradas foram: {', '.join(mulheres) if mulheres else 'Nenhuma'}")

acima_da_media = [p for p in pessoas if p['idade'] > media]
print("D) Lista de pessoas com idade acima da média:")
for p in acima_da_media:
    print(f"   Nome: {p['nome']}; Sexo: {p['sexo']}; Idade: {p['idade']}")
