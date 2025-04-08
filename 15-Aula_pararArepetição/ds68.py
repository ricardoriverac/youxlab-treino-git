from random import randint
v=0
while True:
    print('~'*10)
    jogador=int(input(('Digite um valot: ')))
    print('~'* 10)
    computador=randint(0 , 11)
    total=jogador+computador
    tipo=' '
    while tipo  not in 'PI':
        tipo =str(input('Par ou Impar? [P/I] ')).strip().upper()
    print('_'* 10)
    print(f'Você jogou {jogador}  e o computador {computador}.Total de  {total}')
    print('DEU PAR ' if  total %  2  == 0  else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU')
            v+= 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU')
            v+=1
        else:
            print('VOCÊ PERDEU')
            break
print('Vamos jogar novamente!!')
