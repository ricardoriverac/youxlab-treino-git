dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('E quantos Km vocẽ rodou? '))
precodia = dia*60
precokm = float(km*0.15)
soma = precodia+precokm
print(f'O total a pagar é de R${soma}')