
pesoPessoas = []
pesoPessoasPesadas = []
maiorPeso = 0
pessoaMaisPesada = ''
pessoaMaisLevePeso = 9999999999
nomePessoaLeve = ''
pessoasPesadas = []
pessoasLeves = []
pesoPessoasLeves = []
while True:
    nome = str(input("Digite o nome da pessoa: "))
    pesoPessoas.append(nome)
    peso = float(input(f'Digite o peso de {nome}: '))
    pesoPessoas.append(peso)
    if peso > maiorPeso:
        maiorPeso = peso
        pessoasPesadas.append(nome)
        pessoasPesadas.append(peso)
    else:
        if peso < pessoaMaisLevePeso:
            pessoaMaisLevePeso = peso
            pessoasLeves.append(nome)
            pessoasLeves.append(peso)


    if nome == 'pare':
        break
        # pessoaMaisPesada = nome
    # if peso < pessoaMaisLevePeso:
    #     pessoaMaisLevePeso = peso
    #     pessoasLeves.append(nome)
    #     pesoPessoasLeves.append(peso)

        # nomePessoaLeve = nome
print(f'As pessoas mais pesadas são {pessoasPesadas}')
print(f"{len(pesoPessoas)} foram cadastradas")
# print(f'A pessoa mais pesada é {pessoaMaisPesada} com {maiorPeso}kg')
print(f'A pessoa mais leve é {pessoasLeves}')