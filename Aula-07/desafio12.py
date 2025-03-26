#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

decisao = str(input("Você deseja comprar qual produto? ")).lower()
#.lower() converte o texto para minusculo tipo "ArRoZ"

valorArroz = 47.95
valorFeijao = 8.59
valorMacarrao = 5.92

desconto = 5 / 100

if decisao == "arroz":
    precoFinal = valorArroz - (valorArroz * desconto)
    print("O preço do arroz era R${}, com desconto de 5%, agora custa R${}.".format(valorArroz, precoFinal))

elif decisao in ["feijao", "feijão"]:
    precoFinal = valorFeijao - (valorFeijao * desconto)
    print("O preço do feijão era R${}, com desconto de 5%, agora custa R${}.".format(valorFeijao, precoFinal))

elif decisao in ["macarrao", "macarrão"]:
    precoFinal = valorMacarrao - (valorMacarrao * desconto)
    print("O preço do macarrão era R${}, com desconto de 5%, agora custa R${}.".format(valorMacarrao, precoFinal))

else:
    print("Esté produto, não existe. ou está indisponível")