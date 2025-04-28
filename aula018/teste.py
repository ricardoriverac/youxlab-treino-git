# teste = []
# teste.append('Nicolas')
# teste.append(17)


# tudo =[]
# tudo.append[teste[:]]
# teste[0] = 'Maria'
# teste[1] = 22
# tudo.append(teste[:])
# print(tudo)

# pessoal=[['Nicolas',17],['Gabriel ',20],['Oliveira ',22],['Nolan ',30]]

# print(pessoal[3] [1])

# for posicao in pessoal:
#     print(f'{posicao[0]} tem {posicao[1]} anos de idade ')

galera=[]
dado = []

for contador in range(0,3):

    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:

    if p[1] >= 21:

        print(f'E maior de idade: {p[0]}')
    else:
        print(f'E menor de idade: {p[0]}')

        




