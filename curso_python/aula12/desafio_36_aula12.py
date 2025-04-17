valorCasa = int(input('Quanto vale a casa? '))
valorSalario = int(input('Qual é o valor do salário? '))
quantosAnos = int(input('Em quantos anos deseja pagar? '))
prestacaoMensal = valorCasa / quantosAnos * 12
if prestacaoMensal <= valorSalario * 0.30:
    print ('Parábens! Seu empréstimo foi aceito. ')
else:
    print ('Empréstimo não autorizado. ')