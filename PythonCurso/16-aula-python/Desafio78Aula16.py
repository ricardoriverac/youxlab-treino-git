listanum = []
mai =0
meno=0
for c in range (0,  5):
    listanum.append(int(input(f'Digie um valor  para a posiçao {c}: ')))
    if c ==0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai=listanum[c] 
        if listanum[c]  < men:
            men = listanum[c] 
print('-=' *20) 
print(f'Você digitou os valores: {listanum}')
print(f'O maior valor digitado foi {mai} nas posições', end = ' ')
for i , v  in  enumerate(listanum):
    if v ==mai:
        print(f'{i}...', end = ' ')
print()
print(f'O menor valor digitado foi {men} nas posições ', end =' ')
for i ,  v in enumerate(listanum):
    if v == men :
        print(f'{i}...', end='')
print()