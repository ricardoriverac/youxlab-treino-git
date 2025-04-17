#P.A COM WHILE
termo1=int(input('Digite o 1° termo:'))
razao=int(input('Digite sua razão:'))
termo=termo1
contador=1
total=0
mais=10
while mais!=0:
    total=total+mais
    while contador<=total:
        print(f'{termo} --> ',end='')
        termo+=razao
        contador+=1
    print('Pausa')
    mais=int(input('Quer mostrar mais termos? Digite quantos termos:'))
print(f'Fim! o total de termos mostrados foi de {total}')