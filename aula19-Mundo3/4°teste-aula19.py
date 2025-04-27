brasil=[]
estados1={'estado':'Minas Gerais', 'sigla':'MG'}
estados2={'estado':'Ceará', 'sigla':'CE'}

brasil.append(estados1)  #Adicionou o dicionário estado1 na lista brasil
brasil.append(estados2)  #Adicionou o dicionário estado2 na lista brasil

print(brasil)  #aparece os 2 dicionários em uma lista
print(estados1) #somente estado1
print(estados2) #somente estado2

print(brasil[0]['estado'])  #estado do dicionário com índice 0 dentro da lista brasil
print(brasil[1]['sigla'])  #sigla do dicionário com índice 1 dentro da lista brasil
