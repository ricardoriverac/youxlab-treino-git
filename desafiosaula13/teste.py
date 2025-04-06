for c in range(0 , 6):
    print('Oi')

for c in range(0 , 7, 2):
    print(c)

# n = int(input('Digite um número inteiro: '))
i = int(input('Ínicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n 
print('O somatório de todos valores é {} '.format(s))


