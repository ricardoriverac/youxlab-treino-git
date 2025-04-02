from time import sleep
print ('\033[35m' 'VOCÊ VAI COMPRAR UMA CASA? ' '\033[m')
valor = float(input('Qual é o valor da casa?: '))
salario = float(input('Qual o valor do seu salário?: '))
anos = int(input('Em quantos anos você vai pagar?: '))
print('{}PROCESSANDO...{}'.format('\033[34m', '\033[m'))
sleep(3)
prestacao = anos*12
min = salario*30/100
parcela = valor/prestacao
if parcela>=min:
    print('Seu empréstimo foi {}NEGADO!'.format('\033[31m'))
else:
    print('Seu empréstimo foi {}ACEITO! '.format('\033[32m'))
