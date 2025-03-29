pa = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
soma = pa + (11 - 1) * razao
for c in range(pa,soma + pa ,razao):
    print(f' {c}',end="-> ")
print('\033[31mAcabou\033[m')