a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
print('\033[4mEsses são os 10 primeiros termos da PA:\033[m')
an = a1 + (11 - 1) * r
for n in range(a1, an, r):
    print(f'{n} \033[1;31m->\033[m' , end='')