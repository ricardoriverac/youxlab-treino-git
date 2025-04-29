preço= float(input("Insira o preço do produto: "))
forma= str(input("forma de pagamento")).strip()
vista= preço - (preço*10/100)
vistacart= preço - (preço*5/100)
tresvezes= preço - (preço*20/100)
if forma == "dinheiro":
    print("A vista vai ficar com 10% de desconto foi para {}R$".format(vista))
elif forma == "cartão":
    print("A vista no cartão, vai ficar {}R$".format(vistacart))
elif forma == "2 vezes no cartao":
    print("O preço em duas vezes no cartão vai ficarcom preço normal {}R$".format(preço))
elif forma == "3 vezes no cartao":
    print("3 vezes no cartao vai ficar com juros de 20%{}R$ ,".format(tresvezes))
    