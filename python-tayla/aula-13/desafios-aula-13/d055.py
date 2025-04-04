maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if maior == 0 or peso > maior:
        maior = peso
        maiorPessoa = c
    if menor == 0 or peso < menor:
        menor = peso
        menorPessoa = c
print(f'O maior peso é a {maiorPessoa}° pessoa com valor = {maior}')
print(f'O menor peso é a {menorPessoa}° pessoa com valor = {menor}')