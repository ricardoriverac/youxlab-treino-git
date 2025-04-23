teste= list()
teste.append('Gustavo')
teste.append(40)
galera= list()
galera.append(teste)
teste[0]=' maria'
teste[1]= 22
galera.append(teste)
print(teste)
galera = list()

dado = list()

totmai = totmen = 0

for c in range(0, 3):

  dado.append(str(input('Nome:')))

dado.append(int(input('Idade: ')))

galera.append(dado[:])

dado.clear()
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:  
        print(f'{p[0]} e menor de idade')
        totmai+=1
print(f'Temos (totmai maiores e (totmen) menores de idade.')