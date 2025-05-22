import moeda

while True:
    p = float(input('\nDigite um preço (ou 0 para sair): R$ '))
    
    if p == 0:
        print("Encerrando o programa.")
        break
    
    converter = input("Deseja converter para dólar? [S/N] ").strip().lower()
    
    if converter == 's':
        cotacao = 5.74
        valor_dolar = moeda.converter_para_dolar(p, cotacao)
        print(f'O valor de {moeda.moeda(p)} equivale a ${valor_dolar:.2f} Dólar.')
    
    print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
    print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')