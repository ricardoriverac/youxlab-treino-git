# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora
# a possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# tambem uma função leiafloat() com a mesma funcionalidade.

def linha():
    print("\n")

def cabecalho(mensagem):
    largura = len(mensagem) + 8
    print("~" * largura)
    print(f"{mensagem.center(largura)}")
    print("~" * largura)

def leiaInt(mensagem):
    while True:
        try:
            num = int(input(mensagem)).strip()
        except ValueError: # Se a conversão falhar
            print("ERRO! Digite um número inteiro válido.")
        else: 
            return num # Se der certo, retorna o número
        
def leiaFloat(mensagem):
    while True:
        try:
            num = float(input(mensagem)).strip()
        except ValueError:
            print("ERRO! Digite um número real válido.")
        else:
            return num
        
linha()
cabecalho("Números Inteiros e Reais")
linha()

inteiro = leiaInt("Digite um número inteiro: ")
real = leiaFloat("Digite um número real: ")

print(f"\nO valor inteiro digitado foi {inteiro}")
print(f"O valor real digitado foi {real}\n")