teste=list()
teste.append('Gustavo')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] =  22
galera.append(teste[:])

print(teste)

galera= [['kert' , 1987], ['seabra' , 12], ['Joao' , 34]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print(galera[0])
