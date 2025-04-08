print('fale um PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
tr = 0
while tr < 10:
    tr += 1
    termo = primeiro + (tr - 1) * razão
    print('{}'.format(termo), end=' → ')
print('fim')