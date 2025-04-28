#fazendo cópia de uma lista dentro de outra lista
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #faz uma cópia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# #fatiando uma lista
galera = [['João', 19], ['Ana',33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])

#coloca as informações em forma de lista 
galera = [['João', 19], ['Ana',33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0]) #assim mostra só os nomes
    print(p[1]) #mostra só as idades
    print(f'{p[0]} tem {p[1]} anos de idade.') #mostra bonitinho

#cria lista pedindo nome e idade e mostrando quem é maior e menor de idade
galera = []
dado = []
totalMaior = totalMenor = 0
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # se não colocar os : ele cria listas vazias
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalMenor +=1

print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade')