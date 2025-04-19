ListaPrincipal = []
lista1 = []
lista2 = []
lista3 = []
for a in range (0, 3): lista1.append(int(input(f'Digite um número para [0, {a}]: ')))
for b in range (0, 3): lista2.append(int(input(f'Digite um número para [1, {a}]: ')))
for c in range (0, 3): lista3.append(int(input(f'Digite um número para [2, {a}]: ')))
ListaPrincipal = [lista1, lista2, lista3]
print('=-='*30,f'\n{ListaPrincipal[0]}',f'\n{ListaPrincipal[1]}',f'\n{ListaPrincipal[2]}')
#Não consegui colocar cada número em "[]" :(
    
#Código abaixo é do Guanabara!!    
# matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]')) 
# print('-='*30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l] [c]:^5}]', end='')
#     print()
        