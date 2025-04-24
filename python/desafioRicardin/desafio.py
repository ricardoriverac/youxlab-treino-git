import moeda

while True:
    p = float(input('\nDigite um preço (ou 999 para sair): R$ '))
    if p == 999:
        print("Encerrando o programa.")
        break

converter = input("Deseja converter para dólar? [S/N] ").strip().lower()
if converter == 'S':
        cotacao_dolar = float(input("Digite a cotação do dólar: R$ "))
        valor_dolar = moeda.converter_para_dolar(p, cotacao_dolar)
        print(f'O valor de R$ {moeda.moeda(p)} equivale a ${cotacao_dolar:.2f} Dolar.')
        print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
        print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')