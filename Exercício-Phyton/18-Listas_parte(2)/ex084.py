lista = list()
dados = list()
cont = 0 
pesoMenor = pesoMaior = 0
pessoaMaior = ''
pessoaMenor = ''
while True:
    dados = str(input('Digite o nome: '))
    peso = int(input('Digite o peso: '))
    lista.append(dados)
    lista.append(peso)
    cont+=1
    if peso > pesoMaior:
          pesoMaior = peso
          pessoaMaior = dados
    elif pesoMenor < peso:
          pesoMenor = peso
        
          
    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input(f'Não temos a opçao : {escolha}Quer continuar? [S/N]: ')).upper()
    if escolha == 'N':    
            break
    
print(f'Temos {cont} pessoas cadastradas. ')
print(f'O maior peso é de {pesoMaior} do {dados}')
print(f'O menor peso é de {peso}')
print(lista)

