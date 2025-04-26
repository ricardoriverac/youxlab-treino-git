#EXTRAINDO DADOS DE UMA LISTA
lista=[]
count=1
while True:
        lista.append(int(input('Digite um número: ')))
        escolha=' '
        while escolha not in 'SN':
                escolha=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
                if escolha=='S':
                       count+=1
        if escolha=='N':
            break
lista.sort()
print(f'Você digitou {count} elementos')
print(f'A lista em ordem crescente: {lista}')
if 5 in lista:
       print('O n°5 faz parte da lista!')
else:
       print('Não tem n°5 na lista!')