import moedas

valor = float(input('Digite o preço R$: '))
porcentagem = float(input('Digite um valor R$: '))

print(f'Com {porcentagem} de taxa o valor final sera de {moedas.aumentar(valor,porcentagem,True)} ')

print(f'A metade desse valor e {moedas.metade(valor,True)} ')

print(f'O dobro sera de {moedas.dobro(valor,True) } ') 

print(f'Se diminuirmos o valor pela taxa dita temos {moedas.diminuir(valor,porcentagem,True)}')

