#Verificando empéstimos 
valor=float(input('Qual o preço da sua casa?:'))
salario=float(input('Quanto é o seu sálario?:'))
pagamento=int(input('Em quantos anos você pretende financiar?:'))
prestacao= valor/(pagamento*12)
if prestacao>(0.3*salario):
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido!')
    print(f'Para uma casa de {valor} com financiamento de {pagamento} anos o valor das parcelas será de: {prestacao}')