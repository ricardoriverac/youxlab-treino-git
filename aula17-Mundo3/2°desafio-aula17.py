#VALORES ÚNICOS EM UMA LISTA
valores=[]
while True:
    numero=int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        print('Foi adicionado!')
    else:
        print('Valor já existente!')
    escolha=' '
    while escolha not in 'SN':
        escolha=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha=='N':
        break
valores.sort()
print(valores)