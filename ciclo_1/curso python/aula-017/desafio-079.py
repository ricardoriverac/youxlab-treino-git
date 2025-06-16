lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Ok')
    else:
        print('Este valor já existe na lista! ')
        continuar = str(input('Você quer continuar? S/N:')).upper()
        if continuar == 'N':
            break
print('-=' * 30)
print(f'Você digitou os valores: {lista}')
print('-=' * 30)

