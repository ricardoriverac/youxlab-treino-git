cont = 0
soma = 0
for quantidade in range (1, 7):
    text = (int(input(f'insira o {quantidade} número: ')))
    soma = soma + quantidade
    cont = cont + 1
print(f'a soma dos números indicados é de {soma}')
