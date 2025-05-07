#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar()
#diminuir(), dobro() e metade()

import moeda

din = int(input("Digite um valor: "))
print(f"\nPreço pela metade, resulta em {moeda.metade(din):.0f}")
print(f"Preço dobrado, resulta em {moeda.dobro(din):.0f}")
print(f"Preço aumentado 15%, resulta em {moeda.aumentar(din):.0f}")
print(f"Preço diminuindo 15%, resulta em {moeda.diminuir(din):.0f}\n")
