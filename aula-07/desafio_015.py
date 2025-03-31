dias = float(input('Quantos dias de viagem: '))
km = float(input('Km rodados: '))
vcarro = 60*dias
vkm = 0.15*km
vtotal = vcarro+vkm
print('Custo com carro: R${:.2f}\nCusto em km rodado: R${:.2f}\nValor total do aluguel: R${:.2f}'.format(vcarro, vkm, vtotal))
pgdindin = vtotal-(vtotal*10/100)
pgcartao = vtotal
print('As formas de pagamento serão:\n\nDébido (10% desconto) =   R${:.2f}\n\nCartão (até 3x s/juros) =   R${:.2f}'.format(pgdindin, pgcartao))