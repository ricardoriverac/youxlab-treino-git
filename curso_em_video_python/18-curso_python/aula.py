teste = list()
teste.append('Ana Clara')
teste.append(16)
galera = list()
galera.append(teste[:])
teste [0] = 'Maria Luiza'
teste [1] = '16'
galera.append(teste)
print(galera)

galera = [['Ana Clara', 16], ['Maria Luiza', 16], ['Henrique', 18], ['Helena', 9]]
print (galera[0][1])
print (galera[1][0])

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')