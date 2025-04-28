import moedas

valor = float(input('Digite o preço R$: '))
porcentagem = float(input('Digite um valor R$: '))

print(f'Com {porcentagem} de taxa o valor final sera de {moedas.moeda(moedas.aumentar(valor,porcentagem))}')

print(f'A metade desse valor e {moedas.moeda(moedas.metade(valor))}')

print(f'O dobro sera de {moedas.moeda(moedas.dobro(valor))}') 

print(f'Se diminuirmos o valor pela taxa dita temos {moedas.moeda(moedas.diminuir(valor,porcentagem))}')

