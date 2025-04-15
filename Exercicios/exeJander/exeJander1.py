# Crie um lista, peça pro usuario digitar 6 palavras e salve na lista. depois crie
# um dicionario com quantas vezes cada palavra aparece. exemplo:
# Saida experada:
# {"maça":3, "banana":2, "laranja":1}

from time import sleep

def linha():
    print("\n")

def cabecalho(titulo):
    largura = len(titulo) + 8
    print("~" * largura)
    print(f"{titulo.center(largura)}")
    print("~" * largura)

frutas = []
dados = {}

cabecalho("DIGITE 6 FRUTAS")
linha()
sleep(1)

for f in range(6):
    cabecalho(f"QUAL SERÁ A FRUTA {f+1}")
    linha()
    qualFrutas = input("Digite uma fruta: ").strip().lower()
    frutas.append(qualFrutas)

for f in frutas:
    print(f) # printar/contar a lista de frutas os valores
    if f not in dados:
        dados[f] = 1
    else:
        dados[f] += 1
        
print(dados)
