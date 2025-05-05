#CAIXA ELETRÔNICO
nota200=nota100=nota50=nota20=nota10=nota5=nota1=0
valor=int(input('Digite o valor que você quer sacar: '))
while True:
    if valor>=200:
        valor-=200
        nota200+=1
    elif valor>=100:
        valor-=100
        nota100+=1
    elif valor>=50:
        valor-=50
        nota50+=1
    elif valor>=20:
        valor-=20
        nota20+=1
    elif valor>=10:
        valor-=10
        nota10+=1
    elif valor>=5:
        valor-=5
        nota5+=1
    elif valor>=1:
        valor-=1
        nota1+=1
    if valor==0:
        break
print(f'{nota200} notas de 200, {nota100} notas de 100, {nota50} notas de 50, {nota20} notas de 20, {nota10} notas de 10, {nota5} notas de 5, e {nota1} moedas de 1')

