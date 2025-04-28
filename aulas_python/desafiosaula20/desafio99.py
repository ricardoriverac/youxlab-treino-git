from time import sleep
def maior(* num):
    total = maior = 0
    print('-='*30)
    print('Analisando os valores... ', end='')
    
    if len(num) == 0:
        print('\nNão foi informado \033[33mnenhum valor\033[m')
    else:
        for valor in num:
            print(f'{valor}', end=' ', flush=True)
            sleep(0.5)
            if total == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
            total+=1            
        
        print(f'\nForam informados {total} \033[36mnúmeros\033[m ao todo ')
        print(f'O \033[35mmaior número\033[m é {maior} ')   
        print()
    print('-='*30)
maior(1, 4, 5, 7, 8, 9)
maior(1, 4, 8)
maior(7, 8)
maior(1)
maior()
