tempo = int(input('Qual a idade do seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('Carro velho')
print('Fim!')

print('carro novo' if tempo <=3 else 'Carro velho!')