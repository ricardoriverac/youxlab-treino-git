# Resumão sobre Tuplas em Python

# As tuplas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável.
# Diferente das listas, as tuplas são imutáveis, ou seja, não podem ser modificadas após a criação.

# ---
# 1. Criando Tuplas

lanche = ("Hambúrguer", "Suco", "Pizza", "Sorvete")
print("lanche:", lanche)  # Saída: ('Hambúrguer', 'Suco', 'Pizza', 'Sorvete')

# Também podemos criar tuplas sem parênteses:
lanche = "Hambúrguer", "Suco", "Pizza", "Sorvete"
print("Tipo da variável lanche:", type(lanche))  # Saída: <class 'tuple'>

# ---
# 2. Acessando Elementos

print("Primeiro item:", lanche[0])  # Saída: Hambúrguer
print("Terceiro item:", lanche[2])  # Saída: Pizza
print("Último item:", lanche[-1])  # Saída: Sorvete
print("Penúltimo item:", lanche[-2])  # Saída: Pizza

# ---
# 3. Fatias (Slicing)

print("Elementos do índice 1 ao 2:", lanche[1:3])  # Saída: ('Suco', 'Pizza')

# ---
# 4. Percorrendo Tuplas com For

for comida in lanche:
    print(f"Eu vou comer {comida}")

print("\n")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

print("\n")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print("\nComi muito.")

# ---
# 5. Deletando Tuplas

pessoa = ("João", 17, "M", 50)
del(pessoa)  # Deleta a tupla inteira

# Obs: Não é possível deletar elementos individuais de uma tupla pois ela é imutável.
