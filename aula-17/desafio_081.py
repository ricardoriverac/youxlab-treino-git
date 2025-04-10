valores = []

while True:
    while True:
        try:
            n = int(input('Digite um valor: '))
            valores.append(n)
            break
        except ValueError:
            print('Valor inválido. ', end='')

    while True:
        resp = input('Deseja continuar?[S/N]: ').strip().upper()
        if resp in 'SN':
            break
        else:
            print('Resposta inválida. ', end='')

    if resp == 'N':
        break
    print('-' * 30)

valores.sort(reverse=True)

print('-=' * 30)
print(f'Números digitados: {len(valores)}')
print(f'Lista decrescente dos valores digitados: {valores}')
if valores.count(5) > 0:
    print(f'Há {valores.count(5)} número(s) 5 na lista.')
else:
    print('Não há nenhum número 5 na lista.')
