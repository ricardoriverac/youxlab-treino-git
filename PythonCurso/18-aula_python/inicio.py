#galera = [['Gustavo', 17],['Ana', 17],['João', 19],['Carlos',40]]
#print(galera[3][1])
#for p in galera:
    #print(f'{p[0]} tem {p[1]}, de idade! ')
    #print(p)

#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Olocoo'
#teste [1] = 22
#galera.append(teste[:])
#print(galera)

galera = list()
dado = list()
totamai = totamen = 0
for c in range(0, 3):
    dado.append(str(input('Qual seu nome? ')))
    dado.append(int(input('Qual sua idade? ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totamai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totamen +=1
print('='*20)
print(f'Temos {totamai} maiores de idade e {totamen} menores de idade')