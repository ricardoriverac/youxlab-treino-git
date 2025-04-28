valorcasa=float(input('Qual o valor da casa?  '))
salario=float(input('Quanto você recebe por mês ?  '))
anos=int(input('Em quantos anos pretende pagar a casa?  '))
ani=anos * 12 
men= salario * 0.3
vlr= valorcasa / 12
if men>vlr:
    print('Aprovado')
else:
    print('Negado')