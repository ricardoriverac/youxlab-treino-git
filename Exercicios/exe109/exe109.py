#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro
#a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
#desenvolvida no desafio 108

import moeda

din = int(input("Digite um valor: "))

while True:
    pergunta = input("Você deseja formatar a moeda? [S/N]: ").strip().upper()
    if pergunta in ["S", "N"]:
        break
    else:
        print("\nResposta inválida. Digite apenas S ou N.\n")

if pergunta == "S":
    formatar = True
else:
    formatar = False

print(f"\nPreço pela metade, resulta em {moeda.metade(din, formatar)}")
print(f"Preço dobrado, resulta em {moeda.dobro(din, formatar)}")
print(f"Preço aumentado 15%, resulta em {moeda.aumentar(din, formatar)}")
print(f"Preço diminuído 15%, resulta em {moeda.diminuir(din, formatar)}\n")
