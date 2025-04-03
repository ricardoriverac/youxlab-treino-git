numero=int(input('Digite um número: '))
unidade= numero // 1 % 10
dezena= numero // 10 % 10
centena= numero // 100 % 10
mihar= numero // 1000 % 10
print(f'Unidade:{unidade}')
print(f'Dezena:{dezena}')
print(f'Centena:{centena}')
print(f'Milhar:{mihar}')