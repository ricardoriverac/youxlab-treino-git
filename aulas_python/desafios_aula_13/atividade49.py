print('\033[1;34m-=-=-=-=-= Bem vindo(a)! =-=-=-=-=-\033[m')

n = int(input('Qual número você gostaria de ver a tabuada? '))
for c in range(0, 11,):
    m = c*n
    print('{} x {} = {}'.format(n, c, m))

print('\033[1;34m-=-=-=-=-= FIM! =-=-=-=-=-\033[m')