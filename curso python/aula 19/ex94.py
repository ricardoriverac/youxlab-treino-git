pessoas = []
somaIdades = 0
while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ").strip()
    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo in ['M', 'F']:
            pessoa['sexo'] = sexo
            break
        print("Sexo inválido! Digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    somaIdades += pessoa['idade']
    pessoas.append(pessoa)
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == 'S':
        continue
    else:
        while continuar not in ['S', 'N']:
            continuar = input("Opção inválida. Deseja continuar? [S/N]: ").strip().upper()
        if continuar == 'N':
            break
total = len(pessoas)
if total > 0:
    media = somaIdades / total
else:
    media = 0
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
acimaMedia = [p for p in pessoas if p['idade'] > media]
print('\n' + '\033[35m-\033[m'*40)
print(f"Total de pessoas cadastradas: {total}")
print('\n' + '\033[35m-\033[m'*40)
print(f"Média de idade do grupo: {media:.2f}")
print('\n' + '\033[35m-\033[m'*40)
if mulheres:
    print('\n' + '\033[35m-\033[m'*40)
    print("Mulheres cadastradas:", ', '.join(mulheres))
else:
    print("Nenhuma mulher cadastrada.")
print('\n' + '\033[35m-\033[m'*40)
print()
print("Pessoas com idade acima da média:")
if acimaMedia:
    for p in acimaMedia:
        print(f" - {p['nome']}, {p['idade']} anos")
else:
    print('\n' + '\033[35m-\033[m'*40)    
    print("Nenhuma pessoa com idade acima da média.")
    print('\n' + '\033[35m-\033[m'*40)
