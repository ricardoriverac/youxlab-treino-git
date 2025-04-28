teste = list()
teste.append('Gustavo')
teste.append(40)
# print(teste)
galera = list()
galera.append(teste[:])
# print(galera)
teste [0] = 'Maria'
teste [1] = 22
galera.append(teste)
print(galera)

galeraTeste = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galeraTeste[2] [1])
for p in galeraTeste:
    print(f'{p[0]} tem {p[1]} anos de idade ')
    
galeraTesteDois = list()
dado = list()
for n in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galeraTesteDois.append(dado[:])
    dado.clear()
print(galeraTesteDois)
totalMenor = totalMaior = 0
for p in galeraTesteDois:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade ' )
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade ')
        totalMenor += 1
print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade')


