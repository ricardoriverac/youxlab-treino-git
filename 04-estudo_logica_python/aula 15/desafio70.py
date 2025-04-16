nomeBarato=''
soma = mCaro = mBarato = 0
while True:
    nome= str(input('Informe o nome do produto: '))
    preco = float(input('Digite o preço: '))
    soma += preco
    if preco > 1000:
        mCaro+=1
    if mBarato == 0:
        mBarato = preco
        nomeBarato = nome
    elif preco < mBarato:
        mBarato = preco
        nomeBarato = nome
    choice = str(input('Gostaria de inserir mais produtos? [S/N]')).strip().upper()

    if choice == "N":

        print(f'Total gasto: R${soma:.2f}')
        print(f'Produtos que custam mais do que R$1.000 : {mCaro}')
        print(f'O produto mais barato é {nomeBarato}, que custa R$ {mBarato:.2f}   ')
        break