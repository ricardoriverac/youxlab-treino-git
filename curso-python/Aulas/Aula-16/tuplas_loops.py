lanche = ("Hambúrguer", "Suco", "Pizza", "Sorvete")

# Percorrendo a tupla com for
for comida in lanche:
    print(f"Eu vou comer {comida}")

print("\n")

# Percorrendo a tupla com range e len()
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

print("\n")

# Percorrendo a tupla com enumerate()
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print("\nComi muito.")
