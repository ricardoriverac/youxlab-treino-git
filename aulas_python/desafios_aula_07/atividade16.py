d = float (input('Quantos dias você ultilizou o carro?: '))
km = float (input('Quantos km você percorreu?: '))

r = 60
z = 0.15

m = (d*r)
m2 = (km*z)

m3 = m+m2

print('O valor a pagar é R$',m2)
