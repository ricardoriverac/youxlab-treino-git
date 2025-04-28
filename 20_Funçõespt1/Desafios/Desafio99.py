from time import sleep
def maior(*valores):
    print('-='*20)
    print('Analisando valores informados...')
    for valor in valores:
        print(valor, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo')
    if len(valores) <= 0:
        valores = (0, 0)
    print(f'O maior valor informado foi {max(valores)}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()