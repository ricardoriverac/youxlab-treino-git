continuar = 'S'
soma = 0
contadorProdutoMaiorQue1000 = 0
maior = 0
list = [ ]
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
        if preco < MaisBarato:
            MaisBarato == preco
            list[1] == MaisBarato 
print (f"a soma TOTAL de todos os produtos {soma}")
print (f"Quantidade dos produto com maiores preços {contadorProdutoMaiorQue1000}")
print (f"Produto mais barato {MaisBarato}")