n1 = float(input('Por quantos dias voce alugou o carro = '))
n2 = float(input('Quantos kms voce percorreu = '))
d = n1*60
km = n2*0.15
vt = d + km
print(f'O custo de dias rodados sera de R$ {d} e de km rodados sera de R$ {km} o valor total R$ {vt}')