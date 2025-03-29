num = str(input('Digite um numero de 0 a 9999:'))
n1 = num.strip()

an = n1[3]
an2 = n1[2]
an3 = n1[1]
an4 = n1[0]


print('Unidade: {}'.format(an.strip()))
print('Dezena: {}'.format(an2.strip()))
print('Centena: {}'.format(an3.strip()))
print('Milhar: {}'.format(an4.strip()))