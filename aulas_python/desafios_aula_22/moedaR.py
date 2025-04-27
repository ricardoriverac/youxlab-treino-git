def resumo(n, a, r):
        print('-'*30)
        print('       RESUMO DO VALOR')
        print('-'*30)
        
        print(F'Preço analisado:   R${n:.2f}'.replace('.', ','))
        
        dobro = n * 2
        print(f'Dobro do preço:    R${dobro:.2f}'.replace('.', ','))
        
        metade = n /2
        print(f'Metade do preço:   R${metade:.2f}'.replace('.', ','))
        

        porcentagemA = n + (n * a / 100)
        print(f'{a}% de aumento:    R${porcentagemA:.2f}'.replace('.', ','))

        porcentagemD = n - (n * r / 100)
        print(f'{r}% de redução:    R${porcentagemD:.2f}'.replace('.', ','))
        
        print('-'*30)
