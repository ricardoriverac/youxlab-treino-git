km = int(input('Qual é a distância da sua viagem?'))
#cobrança
co = km * 0.50
if km > 200 :
    nvc = co - (co * 10/100)
    print(f'A sua viagem custurá {nvc}')
else: 
    print(f'A sua viagem custurá {co}')    