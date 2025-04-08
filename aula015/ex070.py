print('<>'*10)
print('LOJA DE 1 A 1000')
print('<>'*10)

nome =''
valor=0
total=0

while True:
    maisBarato=valor

    nome=str(input('Nome do produto: '))

    valor=int(input('Ele custa R$:'))

    escolha=str(input('Você quer continuar? [S/N]'))

    total += valor

    if valor < maisBarato:
        maisBarato = valor


    if escolha =='N':
        break

print(f'A soma de todos os produtos {total} o menor valor e {maisBarato}')




    




