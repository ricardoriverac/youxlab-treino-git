n = 0
soma = 0

count = 0

while n != 999:

    n = int(input('Digite outro numero:'))

    soma += n

    count += 1 

soma -= 999
count -=999
print(f'{count} a soma de todos esses números é {soma}')
print(f'Foram digitados {count} números.')

