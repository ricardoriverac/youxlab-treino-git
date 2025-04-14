#P.A
termo1=int(input('Digite o 1° termo:'))
razao=int(input('Digite sua razão:'))
termo10=termo1+(10-1)*razao
for contador in range(termo1,termo10, razao):
    print(f'{contador}', end=' ')