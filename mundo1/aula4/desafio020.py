import random
nome1 = str(("paulo"))
nome2 = str(("jorge"))
nome3 = str(("junior"))
nome4 = str(("AAAAAAA"))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f"a ordem será {lista}")