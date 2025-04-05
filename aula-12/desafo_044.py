from time import sleep

paleta = {"roxo": "\033[1;95m",

          "ciano": "\033[1;96m",

          "branco": "\033[1;97m",

          "vermelho": "\033[1;91m",

          "padrao": "\033[0;0m"}

valor = {"1": 2, "2": 3, "3": 2.5, "4": 5}

produto = {'1': "pipoca", '2': "agua", '3': "biscoito", '4': "arroz"}

print(f'{paleta["roxo"]}='*41, "\n",

      f" "*10, f'{paleta["ciano"]}LOJINHA\n',

      f'{paleta["roxo"]}={paleta["padrao"]}'*40)

print(f'{paleta["ciano"]}-1-  PIPOCA = R$2,00\n'

      f'-2-  AGUA = R$3,00\n'

      f'-3-  BISCOITO = R$2,50\n'

      f'-4-  ARROZ = 5,00{paleta["ciano"]}')

c1 = str(input(f'\n{paleta["roxo"]}Sua escolha:{paleta["padrao"]} ')).lower().strip()

print(f'{paleta["branco"]}vc comprou um(a) {produto[c1]}, ele(a) vale {valor[c1]} reais{paleta["padrao"]}'.upper())

if valor[c1]:

    print(f'{paleta["ciano"]}TEMOS AS SEGUINTES FORMAS DE PAGAMENTO\n'

          f'- 1 -   a vista no dinheiro com 10% de desconto\n'

          f'- 2 -   a vista no cartão com 5% de desconto\n'

          f'- 3 -   2x no cartão sem juros\n'

          f'- 4 -   3x ou mais no cartão com 20% de juros{paleta["padrao"]}')

    a1 = int(input(f'{paleta["branco"]}SUA OPÇÃO: '))

    print(f'PROCESSANDO SEU PAGAMENTO, AGUARDE...{paleta["padrao"]}')

    sleep(3)

    if a1 == 1:

        print(f'{paleta["branco"]}Sua compra de {valor[c1]} Reais ficará por {(valor[c1] - ((valor[c1] * 10) / 100))} reais com 10% de desconto a vista!!')

    elif a1 == 2:

        print(f'Sua compra de {valor[c1]} reais ficará por {valor[c1] - ((valor[c1] * 5) / 100)} reais à vista no cartão com 5% de desconto!!')

    elif a1 == 3:

        print(f'Sua compra de {valor[c1]} reais parcelada em 2x no cartão sem juros ficará por {valor[c1] / 2} reais!!')

    elif a1 == 4:

        p2 = int(input('Em quantas parcelas vai ser sua compra? '))

        if p2 >= 3:

            print(f'Sua compra de {valor[c1]} reais parcelada em {p2}x ficará por {(((valor[c1] / p2) * 20) / 100) + (valor[c1] / p2):.2f} reais\n'

                  f'com 20% de juros!!')

        else:

            print(f'{paleta["vermelho"]}Seu pagamento não pode ser efetuado!! Tente novamente.')

else:

    print(f'{paleta["vermelho"]}Seu pagamento não pode ser efetuado!! Tente novamente.{paleta["padrao"]}')