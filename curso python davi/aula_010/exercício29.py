vl = int(input('quantos km/hr? : '))
ultrapassagem = (vl - 80) * 7.00
if vl > 80 :
    print(f'passou da velocidade, a multa será de R${ultrapassagem:.2f}')
elif vl == 80 :
    print('no limite.')
else:
    print('dentro da devida velocidade.')     