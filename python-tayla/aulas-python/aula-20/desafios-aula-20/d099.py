from time import sleep

def linha():
    print('\033[1m-=\033[m' * 20)

def maior(* numero):
    linha()
    print('Analisando os valores passados...')
    for n in numero:
        print(f'{n}', end =' ', flush = True)    
        sleep(0.5)
    print(f'Foram informados {len(numero)} números')
    maioValor = max(numero)
    print(f'O maior valor informado foi {maioValor}')
    linha()

maior(3, 5, 3, 6, 1)
maior(2, 0, 4)
maior(0)   