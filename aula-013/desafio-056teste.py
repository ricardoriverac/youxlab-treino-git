soma = idade_20 = homem_idade = idadeHomemMaisVelho = 0
homeMaisVelho = ""


for i in range(4):
    nome = str(input('Digite seu nome:'))
    idade = int(input(f'Digite a idade de {nome}:'))
    sexo = input('Digite o sexo F/M:').lower()
    soma += idade
    s = soma / 4
    if sexo == "f" and idade < 20:
        i += 1

    if sexo == "M" and idade > idadeHomemMaisVelho:
        homeMaisVelho = nome
        idadeHomemMaisVelho = idade
print(f'A média de idades dessas pessoa é {s}')

if homeMaisVelho:
    print(f'O homem mais velho é {homeMaisVelho} com {idadeHomemMaisVelho} anos')
else:
    print('Há apenas mulheres neste grupo.') 
    print(f'Há {idade_20} mulheres com menos de 20 anos.')
    
        
