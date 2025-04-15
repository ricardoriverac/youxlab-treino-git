lista_de_precos = [
    ("Arroz", 30),
    ("Feijão", 12),
    ("Macarrão", 9),
    ("Óleo", 7.),
    ("Açúcar", 5)]

# Exibindo os itens formatados
print("LISTA DE PREÇOS")
print("=" * 30)
for item, preco in lista_de_precos:
    print(f"{item:<20} R$ {preco:>5.2f}")
print("=" * 30)