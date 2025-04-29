dados = {}
soma = 0
idade = []
mulheres = []
MaiorMedia = []
while True:

   
    dados['nome'] = str(input('Nome: '))

    idade = int(input('idade: '))       
    idade.append(idade)                
    dados['idade'] = idade              

    soma = sum(idade)                  
    media = soma / len(idade)         

    if dados['idade'] > media:         
        MaiorMedia.append(dados.copy())  

    dados['sexo'] = str(input('sexo[M/F]: ')).upper() 

    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    if dados['sexo'] != 'M' and dados['sexo'] != 'F':
        print('Erro!. Digite apenas M ou F ')
        dados['sexo'] = str(input('sexo[M/F]: ')).upper()

    escolha = str(input('Quer continuar [S/N]: ')).upper()  

    if escolha != 'S' and escolha != 'N':
        print('Erro!!. Digite apenas S ou N')
        escolha = str(input('Quer continuar [S/N]: ')).upper()  

    if escolha == 'N':
        break

print(f'A média de idade e: {media:.2f}')  
print(f'As mulheres foram: {mulheres}')
print(f'Essa e a lista de pessoa com a média de idade maior que o padrão:')
print(f'{MaiorMedia}')