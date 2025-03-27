num = int(input('informe o número: '))
u = num // 1 % 10
c = num // 10 % 10
d = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Milhar: {m}')