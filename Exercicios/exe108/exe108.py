#Adapte o codigo do desafio 107, criando uma função adicional, chamada moeda()
#que consiga mostra o valor como um valor monetario formatado.

import moeda

din = float(input("Digite um valor: R$ "))
print(f"\nPreço pela metade, resulta em {moeda.moeda(moeda.metade(din))}")
print(f"Preço dobrado, resulta em {moeda.moeda(moeda.dobro(din))}")
print(f"Preço aumentado 15%, resulta em {moeda.moeda(moeda.aumentar(din))}")
print(f"Preço diminuindo 15%, resulta em {moeda.moeda(moeda.diminuir(din))}\n")
