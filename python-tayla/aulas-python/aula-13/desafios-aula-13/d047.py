print('Esses são os pares entre 0 e 50: ')
for c in range(0 , 51):
    if c % 2 == 0:
        print(f' {c} \033[1;31m->\033[m' , end='')