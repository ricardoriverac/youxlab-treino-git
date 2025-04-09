pessoasMais18 = 0
homens = []
somaHomens = 0
mulherMenos20 = 0
while True:
    nome = str(input('Digite o nome de uma pessoa:'))
    idade = int(input(f'Digite a idade de {nome}:'))
    sexo = str(input('Digite o sexo dessa pessoa M/F:')).strip().upper()
    if idade > 18:
        pessoasMais18 += 1
    elif sexo == 'M':
        homens.append({'nome': nome, 'idade': idade})
        somaHomens += 1
    continuar = input("Deseja adicionar outra pessoa? (S/N): ").strip().lower()
    if sexo == 'F' and idade < 20:
        mulherMenos20 += 1

    if continuar != 's':
        break
print(f'\nHá {pessoasMais18} pessoas com mais de 18 anos')
print("\nLista de homens cadastrados:")
for homem in homens:
    print(f"{homem['nome']} - {homem['idade']} anos")
print(f'{somaHomens} Homens cadastrados.')
print(f'Há {mulherMenos20} mulheres com menos de 20 anos.')

    