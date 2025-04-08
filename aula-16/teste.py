#Fazendo uma tupla
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

#Lê quantos termos tem em 'lanche'
print(len(lanche))

for posicao, comida in enumerate(lanche):
   print(posicao)

for cont in range(0, len(lanche)):

    #Mostrar 'lanche' na posição 'cont'
    print(f'Vamos comer {lanche[cont]} na mesa {cont}') 

# Deixa 'lanche' organizado em ordem afabética
print(sorted(lanche))