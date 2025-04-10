# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função
# Input do python, só que fazendo a validação para aceitar apenas um valor númerico
# Ex: n = leiaInt("Digite um número: ")

def linha():
    print("\n")

def cabecalho(mensagem):
    largura = len(mensagem) + 8
    print("~" * largura)
    print(f"{mensagem.center(largura)}")
    print("~" * largura)

def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        numero = input(mensagem)
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print("ERRO! Digite um número inteiro válido.")
        if ok:
            break
    return valor

linha()
cabecalho("Números Inteiros")
linha()

numero = leiaInt("Digite um número: ")
print(f"O número digitado foi {numero}")   