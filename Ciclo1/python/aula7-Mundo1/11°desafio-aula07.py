d=int(input('Por quantos dias você alugou o carro?:'))
km=float(input('Quantos kms você rodou?:'))
dias=d*60
kilometros=km*0.15
total=dias+kilometros
input(f'Total a pagar:{total}')