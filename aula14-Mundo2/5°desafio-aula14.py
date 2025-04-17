#P.A COM WHILE
termo1=int(input('Digite o 1° termo:'))
razao=int(input('Digite sua razão:'))
termo=termo1
contador=1
while contador<=10:
    print(f'{termo} --> ',end='')
    termo+=razao
    contador+=1
print('FIM')