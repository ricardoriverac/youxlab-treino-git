numero = int(input('Digite um número de 0 a 9999'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analizando seu número {}'. format(numero))
print('Seu número tem {} unidades'.format(u))
print('Seu número tem {} dezenas'.format(d))
print('Seu número tem {} centenas'.format(c))
print('Seu número tem {} milhar'.format(m))