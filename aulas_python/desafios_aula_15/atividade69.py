print('\033[1;34m-=-=-=-=-= Análise de dados do grupo =-=-=-=-=-\033[m')
#variaveis
contador18 = 0
contadorF = 0
contadorM = 0 

while True:
    print('-------------------------\n   CADASTRE UMA PESSOA\n-------------------------')
    nome = str(input('Olá, qual seu nome? '))
    
    idade = int(input('Qual sua idade: '))
    while idade > 112:
        idade = int(input(f'Você não tem {idade} anos!\nIdade real: '))
    
    sexo = str(input('Qual seu sexo [M/F]: ')).upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'A opção {sexo} não é uma opção!\n[M/F]: ')).upper()
        
    continuar = str(input('-------------------------\nDeseja continuar? [S/N]: ')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input(f'A opção {continuar} não é uma opção!\n[S/N]')).upper()

    if sexo in 'F' and idade < 20:
        contadorF += 1
        
    if sexo in 'M':
        contadorM += 1 
        
    if idade > 18:
        contador18 += 1
        
    if continuar == 'N':
        break
if contadorM > 1:
    print(f'Ao todo temos {contadorM} homens cadastrados!')
    
else:
    print(f'Ao todo temos {contadorM} homem cadastrado!')

print(f'Total de pessoas com mais de 18 anos: {contador18}')
print(f'E temos {contadorF} mulheres com menos de 20 anos!')

print('\033[1;34m-=-=-=-=-= Ate mais...  =-=-=-=-=-\033[m')

