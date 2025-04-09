#Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parametro
#E mostre uma mensagem com tamanho adaptavel.

def escreva(texto):
    largura = len(texto) + 8
    print("\n")
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)
    print("\n")

print("Criação de cabeçalho personalizado")
pergunta = input("Digite o seu título: ")
escreva(pergunta)
