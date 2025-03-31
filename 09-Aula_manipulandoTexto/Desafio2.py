num=int(input('Digite um numero '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('o seu numero e {}'.format(num))
print('A unidade {}'.format(u))
print('A denzena e {} '. format(d))
print('A centena e {}'.format(c))
print('A milhar e {}'.format(m))

