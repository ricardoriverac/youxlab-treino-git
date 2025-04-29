valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor:')))
    
print(f'Você digitou os valores: {valores}')

print(f'O maio número sorteado foi {max(valores)} na posição {valores.index(max(valores))}')

print(f'O menor número sorteado foi {min(valores)} na posição {valores.index(min(valores))}')