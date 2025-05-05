#CALCULANDO FATORIAL
numero=int(input('Digite o número que deseja fatorar: '))
contador=numero
fatorial=1
while contador>0:
    print(f'{contador}', end=' ')
    print('x' if contador>1 else '=',end='')
    fatorial*=contador
    contador-=1
print(f'{fatorial}')