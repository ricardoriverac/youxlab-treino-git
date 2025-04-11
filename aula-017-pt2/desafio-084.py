pesoPessoas = []
maiorPeso = 0
pessoaMaisPesada = ''
pessoaMaisLevePeso = 9999999999
nomePessoaLeve = ''
while True:
    nome = str(input("Digite o nome da pessoa: "))
    pesoPessoas.append(nome)
    if nome == 'pare':
        break
    peso = float(input(f'Digite o peso de {nome}: '))
    pesoPessoas.append(peso)
    if peso > maiorPeso:
        maiorPeso = peso
        pessoaMaisPesada = nome
    if peso < pessoaMaisLevePeso:
        pessoaMaisLevePeso = peso
        nomePessoaLeve = nome
        
    print(f"{len(pesoPessoas)} foram cadastradas")
    print(f'A pessoa mais pesada é {pessoaMaisPesada} com {maiorPeso}kg')
    print(f'A pessoa mais leve é {nomePessoaLeve} com {pessoaMaisLevePeso}kg')