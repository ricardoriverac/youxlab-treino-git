#variaveis
contP = 0
cont1k = 0 
lista = []
lista2 = []
cont = 0

while True:
    print('-------------------------\n   Loja super baratão   \n-------------------------')
    nomep = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    
    escolha = str(input('Quer continuar [S/N] ')).upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input(f'A opção {escolha} não é uma opção!\n[S/N]')).upper()
    
    cont += 1
    lista.append(preco)
    lista2.append(nomep)
    
    if preco > 1000:
        cont1k += 1
    
    if escolha == 'N':
        break

soma = sum(lista)
miN = min(lista2)

print(f'-------------------------\nO total da compra foi: R${soma:.2f}')
print(f'Temos {cont1k} produtos custando mais de R$1000,00 ')
print(f'O produto mais barato foi: {miN} ')
print(f'Você comprou {cont} produtos')