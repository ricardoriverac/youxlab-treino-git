soma = 0
m = 0
for c in range(4):
    num = int(input(f'Digite o {c+1} número: '))
    soma += num

def media(soma, qtd_numeros):
    m = soma / qtd_numeros
    print(f'A média de todos esses números é igual a : {m}')


media(soma=soma, qtd_numeros=4)
  