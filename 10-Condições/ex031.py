distancia = float(input('Quantos Km de distancia voce irá viajar?: '))

if distancia < 200:
    pago = distancia * 0.50 
    print(f'Voce irá pagar: {pago}')

else: 
    w = distancia * 0.245
    print(f'O preço a pagar será:{w}')


