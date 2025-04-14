continuar = 'S'
soma = 0
contadorProdutoMaiorQue1000 = 0
maior = 0
list = [ ]
MaisBarato = 0
while continuar == "S":
    nomeProduto = str (input ("Qual o nome do produto ? "))
    preco = int (input ("Qual é o preço do produto ? "))
    continuar = str (input ("Quer continuar [S/N] ? ")).upper()
    soma = preco + soma
    list.append(nomeProduto)
    list.append(preco)
    if preco > 1000:
        contadorProdutoMaiorQue1000 += 1
    if len (nomeProduto) == 0:
        MaisBarato = preco
        preco = list[1]
    else:
        if list[1] < MaisBarato:
            MaisBarato = list[1]
for p in nomeProduto:
    if p[1] == MaisBarato:
        print (f"{p[0]}")
print (f"a soma TOTAL de todos os produtos {soma}")
print (f"Quantidade dos produto com maiores preços {contadorProdutoMaiorQue1000}")
print (f"Produto mais caro {MaisBarato}")