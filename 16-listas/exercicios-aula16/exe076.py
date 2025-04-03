itens = ('lapis' , 1 , 'caneta' , 2.50 , 'borracha' , 5.50 , 'maquina de impressora' , 19.50 )
for c in range(0, len(itens), 2):
    print(f'{itens[c]:.<34} ', end='')
    print(f'R$ {itens[c+1]:>7.2f}')
print('-'*45)