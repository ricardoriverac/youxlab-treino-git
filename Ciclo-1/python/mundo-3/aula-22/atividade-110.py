from utilidadesCeV import moeda

taxa_cambio = 5.73

while True:
    try:
        preco = float(input("Digite o preço: R$ ").replace(',', '.'))
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
        continue

    moeda.resumo(preco, taxa_cambio)

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        print("Encerrando o programa. Até mais!")
        break
