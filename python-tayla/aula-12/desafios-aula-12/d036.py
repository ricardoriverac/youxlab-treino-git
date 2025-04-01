vcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = vcasa / (anos * 12)
if prestacao <= (salario * 0.30):
    print(f'Esse é o valor das prestações: R${prestacao:.2f}')
else:
    print('Você não pode comprar essa casa')