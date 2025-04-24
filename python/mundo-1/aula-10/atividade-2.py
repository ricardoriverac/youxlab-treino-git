km = float(input('Quantos km/h voce estava: '))
velocidade = ((km-80)*7) 
print(f'Voce foi multado e tera que pagar R${velocidade}' if velocidade > 80 else 'Voce não foi multado')