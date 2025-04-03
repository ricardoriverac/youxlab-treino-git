n = int(input('Digite um número: '))
print('Essa é a tabuada dele:')
for c in range(0, 11):
    print(f'{n} x {c} = \033[1;36m{n * c}\033[m')