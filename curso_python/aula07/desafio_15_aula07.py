dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
totalDias = dias * 60
totalKm = km * 0.15
print (f'O total a pagar é R${(totalDias+totalKm):.2f} ')