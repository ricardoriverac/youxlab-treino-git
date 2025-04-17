produtos = [{'nome': 'Guaraná Jesus', 'preço': 5.99}, {'nome': 'Fini', 'preço': 2.50},{'nome':  'Mario Kart', 'preço': 49.99}]
print('=========== Listagem de Preços ==================')
for produto in produtos:
    print(f"Produto: {produto['nome']}  | Preço:  R${produto['preço']}")