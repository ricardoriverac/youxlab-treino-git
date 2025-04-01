print('-=-=-=-=-Digite dois números inteiros para serem comparados-=-=-=-=-')
numero1 = int(input('Seu primeiro número? '))
numero2 = int(input('Seu segundo número? '))

max = max(numero1, numero2)
min = min(numero1, numero2)

print('O maior número é {}'.format(max))
    

print('O menor número é {}'.format(min))
    
if max == min:
    print('Os números {} e {} são iguais :)'.format(numero1, numero2))