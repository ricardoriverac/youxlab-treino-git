print('1°TESTE')
teste=list()
teste.append('Sophia')
teste.append(16)
pessoas=list()
pessoas.append(teste[:])  #foi colocado a lista teste dentro da lista pessoas
teste[0]='Sarah'
teste[1]=16
pessoas.append(teste[:])  #as informações a cima também foram adicionadas na mesma lista pessoas
print(pessoas)

print('2°TESTE')
pessoas=[['Jade',6],['Lua',3],['Estrela',1]]
print(pessoas[0][0])  #na lista 0 printa o elemento 0, neste caso Jade
print(pessoas[1][1])  #na lista 1 printa o elemento1, neste caso 3
print(pessoas[2])  #printa a lista 2 inteira, neste caso Estrela, 1

print('3°TESTE')
pessoas=[['Jade',6],['Lua',3],['Estrela',1]]
for pessoa in pessoas:  #para cada pessoas em pessoas
    print(pessoa[0])  #printa somente o elemento 0, no caso os nomes
for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade') #printa o nome no elemento 0 e a idade no elemento 1

print('4°TESTE')
pessoas=[]
dados=[]  #lista secundária
totalMenor= totalMaior=0
for contador in range(0,4):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite a sua idade: ')))
    pessoas.append(dados[:])
    dados.clear()  #excluido ápos inserida em pessoas
for pessoa in pessoas:
    if pessoa[1]>=21:
        print(f'{pessoa[0]} são maior de idade')
        totalMaior+=1
    else:
        print(f'{pessoa[0]} são menor de idade')
        totalMenor+=1
print(f'Temos {totalMaior} pessoas maior de idade e {totalMenor} pessoas menor de idade') 