somaidade = 0
maioridade = 0
mediaidade = 0
totmulher  = 0
nomevelho = ''
for p in range(1,5):
    print(f'-----{p}° PESSOA-------')
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo == 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade :
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20 :
        totmulher += 1
mediaidade = somaidade / 4 
print(f'A media de todas as idades foi {mediaidade}')
print(f'O homem mais velho foi o {nomevelho} é ele tinha {maioridade}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')