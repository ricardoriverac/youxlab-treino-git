# Resumão sobre Listas em Python

# As listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável.
# Diferente das tuplas, as listas são mutáveis, ou seja, podemos modificar seus elementos após a criação.

# ---
# 1. Criando Listas

lanche = ["Hambúrguer", "Suco", "Pizza", "Sorvete"]
print("lanche:", lanche)  # Saída: ['Hambúrguer', 'Suco', 'Pizza', 'Sorvete']

# Podemos verificar o tipo da variável:
print("Tipo da variável lanche:", type(lanche))  # Saída: <class 'list'>

# ---
# 2. Acessando Elementos

print("Primeiro item:", lanche[0])  # Saída: Hambúrguer
print("Terceiro item:", lanche[2])  # Saída: Pizza
print("Último item:", lanche[-1])  # Saída: Sorvete
print("Penúltimo item:", lanche[-2])  # Saída: Pizza

# ---
# 3. Modificando Listas

lanche[1] = "Refrigerante"
print("Lista modificada:", lanche)  # Agora 'Suco' virou 'Refrigerante'

# ---
# 4. Adicionando Elementos

lanche.append("Batata Frita")  # Adiciona ao final da lista
print("Lista após append:", lanche)

lanche.insert(1, "Hot Dog")  # Insere na posição desejada
print("Lista após insert:", lanche)

# ---
# 5. Removendo Elementos

lanche.remove("Pizza")  # Remove o primeiro elemento com esse nome
print("Lista após remove:", lanche)

lanche.pop()  # Remove o último item
print("Lista após pop:", lanche)

lanche.pop(1)  # Remove o item da posição 1
print("Lista após pop(1):", lanche)

# ---
# 6. Percorrendo Listas

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
# 7. Ordenando Listas

numeros = [3, 1, 4, 1, 5, 9, 2]
numeros.sort()
print("Lista ordenada:", numeros)

numeros.sort(reverse=True)
print("Lista ordenada ao contrário:", numeros)

# ---
# 8. Copiando Listas

lista_original = [1, 2, 3]
lista_copia = lista_original[:]  # Faz uma cópia verdadeira da lista
lista_original.append(4)
print("Lista original:", lista_original)
print("Lista cópia:", lista_copia)

# ---
# 9. Listas aninhadas

lista_aninhada = [[], [], []]

lista_aninhada[0].append("Maçã")
lista_aninhada[1].append("Laranja")
lista_aninhada[2].append("Banana")
print(f"Lista aninhada completa: {lista_aninhada}")