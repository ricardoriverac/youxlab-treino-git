continuar = 'S'
soma = 0
contadorProdutoMaiorQue1000 = 0
menor = 0
nomeMenor = ''
list = []
while continuar == "S":
    nomeProduto = str (input ("Qual o nome do produto ? "))
    preco = int (input ("Qual é o preço do produto ? "))
    continuar = str (input ("Quer continuar [S/N] ? ")).upper()
    soma = preco + soma
    list.append(nomeProduto)
    list.append(preco)
    if preco > 1000:
        contadorProdutoMaiorQue1000 += 1
    if menor == 0:
        menor = preco
        nomeMenor = nomeProduto
    elif menor > preco:
        menor = preco
        nomeMenor = nomeProduto

print (f"a soma TOTAL de todos os produtos: \033[36m{soma}\033[m")
print (f"Quantidade dos produto com preços maiores que 1000: \033[36m{contadorProdutoMaiorQue1000}\033[m")
print (f"Produto mais barato: \033[36m{nomeMenor}\033[m")