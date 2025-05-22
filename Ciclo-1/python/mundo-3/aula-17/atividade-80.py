lista = []

for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    
    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
  
        for j in range(len(lista)):
            if num <= lista[j]:
                lista.insert(j, num)
                print(f'Adicionado na posição {j}.')
                break

print('\nLista ordenada:', lista)
