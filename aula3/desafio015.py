n1 = float(input('quantos dias você alugou o carro? '))
n2 = float(input('quantos km você andou com o carro? '))
d = n1*60
km = n2*0.15
vt = d+km
print(f"você deve pagar R${vt} pelo carro alugado")