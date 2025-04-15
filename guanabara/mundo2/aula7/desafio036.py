#textos
valor = float(input('qual o valor da casa? '))
salario = float(input('quanto você recebe por mês: '))
ano = float(input('em quantos anos você irá pagar: '))

#contas
porcentagem =  salario * (30/100)
if porcentagem > salario:
    print('não será possivel realizar o financiamento')
else:
    prestacao = (valor / ano)/12
    print(f'''O financiamento poderá ser realizado.
          Por mês você pagará R${prestacao}''')