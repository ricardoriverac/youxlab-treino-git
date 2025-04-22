import time
from utilidadesCeV import moeda

cotacao = 5.73330

while True:
    try:
        preco = float(input("Digite o preço: R$ "))
        print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")
        print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")
        print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}")
        print(f"Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}")
        print('-' * 30)

        resp_dolar = str(input("Deseja converter para dólar? [S/N]: ")).strip().upper()
        if resp_dolar == 'S':
            print(f"Valor em dólar: {moeda.dolar(preco, cotacao)}")
            print('-' * 30)

        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
        if resp == 'N':
            time.sleep(1)
            print('=' * 10, 'VOLTE SEMPRE', '=' * 10)
            break
        elif resp != 'S':
            print('Opção inválida. Tente novamente.')

    except ValueError:
        print("Por favor, insira um número válido.")
