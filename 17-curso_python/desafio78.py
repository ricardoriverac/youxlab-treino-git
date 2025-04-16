lista = []
for numeros in range (1,6):
    numero = int(input(f'Digite o {numeros}° número: '))
    lista.append(numero)
    maior = max(lista)
    menor = min(lista)
    posicaoMenor = lista.index(menor)
    posicaoMaior = lista.index(maior)
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
print(f'A posição do número {maior} é {posicaoMaior}')
print(f'A posição do número {menor} é {posicaoMenor}')