cs = float(input('Valor da casa: R$'))
sl = float(input('Salário do comprador: R$'))
fi =  int(input('Quantos anos de financiamento: '))
pr =  cs / (fi * 12)
minimo = sl * 30/100
print(f'Para pagar uma casa de R${cs:.2f} em {fi} anos',end=" ")
print(f' a prestação será de R${pr:.2f}')
if pr > minimo :
    print('EMPRPESTIMO NEGADO')
elif pr < minimo :
    print('EMPRESTIMO CONCEDIDO')
       

