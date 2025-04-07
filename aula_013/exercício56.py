lista_nome = []
lista_nome_homem = []
lista_idade = []
lista_sexo = []
lista_idade_homem = []
lista_idade_mulher = []

for c in range (1,5):

    print('-------------- {}ª pessoa ----------------'.format(c))

    nome = str(input('digite o nome: ')).strip().upper()

    lista_nome.append(nome)


    idade = int(input('digite a idade: '))

    lista_idade.append(idade)

    sexo = str(input('Digite o sexo F/M: ')).strip().upper()

    lista_sexo.append(sexo)

    if sexo == 'M':

        lista_nome_homem.append(nome)
        lista_idade_homem.append(idade)
    if sexo == 'F' and idade < 20:
        lista_idade_mulher.append(idade)

print('a média de idade do grupo é {}'.format(sum(lista_idade)/len(lista_idade)))
print('nome do homem mais velho: {}'.format(lista_nome_homem[lista_idade_homem.index(max(lista_idade_homem))]))
print('o total de mulheres abaixo de 20 anos: {}'.format(len(lista_idade_mulher)))