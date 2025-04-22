import moeda

taxa_cambio = 5.73

while True:
    preco = float(input("Digite o preço: R$ "))

    print(f"A metade de {moeda.formato(preco)} é {moeda.metade(preco, True)}")
    print(f"O dobro de {moeda.formato(preco)} é {moeda.dobro(preco, True)}")
    print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}")
    print(f"Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}")
    print('-'*50)
    print(f"Convertido para Dólar, temos {moeda.converter_para_dolar(preco, taxa_cambio, True)}")
    print('-'*50)


    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar != 'S':
        print("Encerrando o programa. Até mais!")
        break
