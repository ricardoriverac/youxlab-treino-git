print('-=-=-=-= Bem vindo(a) ao nosso plano de empréstimo =-=-=-=-')
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
quantosa = float(input('Em quantos anos você vai pagar: '))

anos = quantosa*12
divisao = valor/anos

print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f} '.format(valor, quantosa, divisao))

if divisao < salario:
    print('Empréstimo aceito!!')
    
else:
    print('Empréstimo não aceito :(')
    