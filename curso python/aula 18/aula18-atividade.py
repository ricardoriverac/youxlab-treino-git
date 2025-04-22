#      LISTAS COMPOSTAS (lista dentro de lista)
#                   [[]]
pessoas = [['pedro', 12], ['Rafaela', 18], ['João', 32]]
print (pessoas[0][0]) # primeira lista e primeiro elemento (pedro)
print (pessoas[1][1]) # segunda lista e segundo elemento (18)
print (pessoas[2][0]) # terceira lista e primeiro elemento (João)
print (pessoas[1]) # imprime tudo da primeira lista (rafaela, 18)
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list ()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
print (galera) # mostra toda essa lista de quatro pessoas
for p in galera:
    print (f'{p[0]} tem {p[1]} anos de idade.') # formatação com nome e idade
galera = list()
dados = list()
totalmaior = totalmenor = 0
for c in range (0,3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()
print (galera)
for p in galera:
    if p[1] >= 21:
        totalmaior += 1
        print (f"{p[0]} é maior de idade")
    else:
        totalmenor += 1
        print (f"{p[0]} é menor de idade")
print (f"o total de maior de idade: {totalmaior}")
print (f"o total de menor de idade: {totalmenor}")
    
    