quilometros = float(input('quantos km/h você estava?: '))
velocidade = ((quilometros-80)*7)
print(f'você terá que pagar R${velocidade} de multa' if quilometros > 80 else "fica de boas")