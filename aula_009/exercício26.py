frase = input("Diga uma frase: ").upper().strip()
print("a frase tem {} Letras a.".format(frase.count("A")))
print("o primeira A apareceu na posicão {}".format(frase.find("A")+1))
print("o ultima  A apareceu na posição {}".format(frase.rfind("A")+1))