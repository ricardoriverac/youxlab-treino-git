Armazenamento = list()
dados = list()

escolha = 'S'
contadorCadastro = 0

print('\033[1;34m-=-=-=-=-= Lista composta e análise de dados =-=-=-=-=-\033[m')

while escolha == 'S':
    dados.append(str(input('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nQual seu nome?: ')))
    
    peso = dados.append(float(input('Qual o seu peso?: ')))
    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    contadorCadastro += 1
    
    Armazenamento.append(dados[:])
    dados.clear()

    #Programa só aceita S ou N se for outra coisa ele recusa
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Opção inválida\n[S/N]: ')).upper()

maior = max(p[1] for p in Armazenamento)
menor = min(p[1] for p in Armazenamento)

#Se apenas uma pessoa for cadastrada ele mostra "Uma" pessoa, se for mais de uma ele printa "pessoas"  
if contadorCadastro == 1:
    print('=-'*20, f'\nAo todo você cadastrou "\033[1;31mUma\033[m" pessoa.')   
else: 
    print('=-'*20, f'\nAo todo você cadastrou {contadorCadastro} pessoas.')

print(F'O maior peso foi de {maior}Kg. Peso de', end='')
for pessoa in Armazenamento:
    if pessoa[1] == maior:
        print(f' [{pessoa[0]}]', end= '')
        
print(F'\nO menor peso foi de {menor}Kg. Peso de', end='')
for pessoa in Armazenamento:
    if pessoa[1] == menor:
        print(f' [{pessoa[0]}]', end= '')
Armazenamento = list
dados = list()

escolha = 'S'
contadorCadastro = 0

print('\033[1;34m-=-=-=-=-= Lista composta e análise de dados =-=-=-=-=-\033[m')

while escolha == 'S':
    dados.append(str(input('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nQual seu nome?: ')))
    
    peso = dados.append(float(input('Qual o seu peso?: ')))
    
    escolha = str(input('Quer continuar? [S/N]: ')).upper()
    contadorCadastro += 1
    
    Armazenamento.append(dados[:])
    dados.clear()

    #Programa só aceita S ou N se for outra coisa ele recusa
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Opção inválida\n[S/N]: ')).upper()

maior = max(p[1] for p in Armazenamento)
menor = min(p[1] for p in Armazenamento)

#Se apenas uma pessoa for cadastrada ele mostra "Uma" pessoa, se for mais de uma ele printa "pessoas"  
if contadorCadastro == 1:
    print('=-'*20, f'\nAo todo você cadastrou "\033[1;31mUma\033[m" pessoa.')   
else: 
    print('=-'*20, f'\nAo todo você cadastrou {contadorCadastro} pessoas.')

print(F'O maior peso foi de {maior}Kg. Peso de', end='')
for pessoa in Armazenamento:
    if pessoa[1] == maior:
        print(f' [{pessoa[0]}]', end= '')
        
print(F'\nO menor peso foi de {menor}Kg. Peso de', end='')
for pessoa in Armazenamento:
    if pessoa[1] == menor:
        print(f' [{pessoa[0]}]', end= '')
