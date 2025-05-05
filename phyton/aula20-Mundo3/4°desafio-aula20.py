
def valores(*numeros):
    print('Analisando valores passados...')
    quantidade= len(numeros)
    print(f'{numeros} Foram informados {quantidade} valores')
    maior=max(numeros)
    print(f'O maior números foi o {maior}')
    print('-'*30)

valores(9,7,0,3,5,8)
valores(4,7,0)
valores(1,2)
valores(6)
valores(0)