dados = {}
soma = 0
idades = []
mulheres = []
mediaMaior = []
while True:

   
    dados['nome'] = str(input('Nome: '))

    idade = int(input('idade: '))       
    idades.append(idade)                
    dados['idade'] = idade              

    soma = sum(idades)                  
    media = soma / len(idades)         

    if dados['idade'] > media:         
        mediaMaior.append(dados.copy())  

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

print()
print('------Resultados------')
print()

print(f'A média de idade e: {media:.2f}')  
print(f'As mulheres foram: {mulheres}')
print(f'Essa e a lista de pessoa com a média de idade maior que o padrão:')
print(f'{mediaMaior}')
