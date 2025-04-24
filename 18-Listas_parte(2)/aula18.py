# dados = list()

# dados.append('Pedro')
# dados.append(25)

# pessoas = list()
# pessoas.append(dados[:])
# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
# print(pessoas[0])

# teste = list()
# teste.append('Fabricio')
# teste.append(40)
# galera= list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 5):
    dado.append(str(input('nome: ')))
    dado.append(int(input('Idade:' )))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
   
    else:
        print(f'{p[0]} é menor de idade. ')
        totmen += 1 

print(f'Temso {totmai}, maiores e {totmen} menores de idade. ')
