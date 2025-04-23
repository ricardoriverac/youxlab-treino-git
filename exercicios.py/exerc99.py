numeros = []
def maior(*num):
    maior = max(numeros)
    print(f'O maior número entre {numeros} é {maior}.')

while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()
        if resposta in 'SN':
            break
        print('Algo deu errado. Tente de novo.', end= ' ')
    if resposta == 'N':
        break
print(f'A quantidade de números digitados foi {len(numeros)}')
maior(numeros)
