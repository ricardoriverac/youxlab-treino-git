nomeBarato=''
soma = mCaro = mBarato = 0
while True:
    nome= str(input('\033[38;5;216mInforme o nome do produto\033[0m: '))
    preco = float(input('\033[38;5;153mDigite o preço\033[0m: '))
    soma += preco
    if preco > 1000:
        mCaro+=1
    if mBarato == 0:
        mBarato = preco
        nomeBarato = nome
    elif preco < mBarato:
        mBarato = preco
        nomeBarato = nome
    choice = str(input('\033[38;5;183mGostaria de inserir mais produtos? [S/N]\n\033[0m: ')).strip().upper()

    if choice == "N":

        print("\033[38;5;216mTotal gasto\033[0m: R${soma:.2f}")
        print(f"\033[38;5;153mProdutos que custam mais do que R$1.000\033[0m: {mCaro}")
        print(f"\033[38;5;183mO produto mais barato é {nomeBarato}, que custa R$\033[0m{mBarato:.2f}")
        print("\033[1;38;5;225mPrograma finalizado!🌸\033[0m")
        break
