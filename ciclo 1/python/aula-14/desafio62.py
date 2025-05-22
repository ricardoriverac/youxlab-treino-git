print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

i = 0

while i < 10:
    i += 1
    termo = primeiro + (i - 1) * razão
    print('{}'.format(termo), end=' - ')
print('Fim')