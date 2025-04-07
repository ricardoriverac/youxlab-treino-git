#separando casas decimais
numero=int(input('Digite um número: '))
unidade= numero // 1 % 10 # dividindo o n° inteiramente por 1 e tiro o modulo de 10 ,ou seja, o resto da divisão é = unidade
dezena= numero // 10 % 10
centena= numero // 100 % 10
mihar= numero // 1000 % 10
print(f'Unidade:{unidade}')
print(f'Dezena:{dezena}')
print(f'Centena:{centena}')
print(f'Milhar:{mihar}')