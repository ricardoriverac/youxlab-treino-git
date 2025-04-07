casa = float(input('Qual o valor da casa? R$ '))
comprador = float(input('Qual é o salário do comprador? R$ '))
anos = float(input('Quantos anos irá durar o pagamento: '))
mensal = casa / (anos * 12)
porcentagem = mensal * 100 / comprador
if mensal <= 0.3 * comprador:
    print('O valor do pagamento mensal de tal imóvel é de R${:.2f}.\nPara o empréstimo ser aprovado o pagamento mensal'
' não deve ser superior a 30% do salário do indivíduo. O resultado foi: {:.2f}%\nSeu empréstimo foi '
'\033[1;32maceito\033[m, parabéns!'.format(mensal, porcentagem))
else:
    print('O valor do pagamento mensal de tal imóvel é de R${:.2f}.\nPara o empréstimo ser aprovado o pagamento mensal'
' não deve ser superior a 30% do salário do indivíduo. O resultado foi: {:.2f}%\nO empréstimo '
'\033[1;31mnão foi aceito\033[m, desculpe.'.format(mensal, porcentagem))