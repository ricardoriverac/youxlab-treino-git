valor = int(input('Valor do saque: '))

cedulas = [50, 20, 10, 1] 
linhalista = 0

while valor > 0:
    cedulaatual = cedulas[linhalista]
    quantidade = valor // cedulaatual

    if quantidade > 0:
        print(f'Total de {quantidade} células de R${cedulaatual}')
    
    valor = valor % cedulaatual
    linhalista += 1