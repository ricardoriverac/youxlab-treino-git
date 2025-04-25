def maior(*valores):
    if len(valores) == 0:
        print('-=-'*15)
        print('Analisando os valores passados...')
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0')
    
    else:
        cont = 0 
        m = valores[0]
        for v in valores:
            cont += 1
            if v > m:
                m = v
        print('-=-'*15)
        print('Analisando os valores passados...')
        print(f'{valores} Foram informados {cont} valores ao todo.')
        print(f'O maior valor informado foi {m}')
        
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior( )