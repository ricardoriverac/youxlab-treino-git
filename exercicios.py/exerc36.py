from time import sleep
print('Você deseja comprar uma casa. Carregando informaçoẽs...')
sleep(1)
valorCasa = float(input("Qual o valor da casa que você planeja comprar? R$"))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
mensal = 12*anos
minimo = salario * 30/100
parcela = valorCasa/mensal 
print('Para pagar uma casa de R${} em {} anos, a prestação será de {:.3f}.'.format(valorCasa, anos, parcela))
if parcela > minimo :
    print('O empréstimo foi \033[1;31mRECUSADO')
else:
    print('O empréstimo foi \033[1;32mACEITO')