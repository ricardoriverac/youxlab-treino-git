# Acessando elementos da tupla
lanche = ("Hambúrguer", "Suco", "Pizza", "Sorvete")

print("Primeiro item:", lanche[0])  # Saída: Hambúrguer
print("Terceiro item:", lanche[2])  # Saída: Pizza

# Acessando elementos de trás para frente
print("Último item:", lanche[-1])  # Saída: Sorvete
print("Penúltimo item:", lanche[-2])  # Saída: Pizza

# Usando fatias (slicing) para obter um subconjunto da tupla
print("Elementos do índice 1 ao 2:", lanche[1:3])  # Saída: ('Suco', 'Pizza')
