pessoas = {}
lista = []
iadadePessoas = []
cont = 0
while True:
    nome = pessoas['nome'] = str(input("Digite o nome: "))
    cont += 1
    idade = pessoas['idade'] = int(input('Digite a idade: '))
    iadadePessoas.append(idade)
    sexo = pessoas['sexo'] = str(input('Qual o sexo? F/M: ')).upper()
    continuar = str(input('Quer continuar? S/N')).upper()
    if continuar == 'N':
        break
    else:
        
