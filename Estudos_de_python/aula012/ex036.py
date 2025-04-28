print('<=>'*20)
emprestimo=float(input('Diga o valor do emprestimo para a compra de sua casaR$: '))
tempo=int(input('Em quantas parcelas pretende pagar?: '))
sal=float(input('Nos informe sua renda  mensalR$: '))
parcela=emprestimo/tempo
parcelaAprovada=parcela*30/100 + parcela

if sal >= parcelaAprovada:
    print('Parabens você pode comprar a casa ')
else:
    print('Você não pode comprar a casa ')
