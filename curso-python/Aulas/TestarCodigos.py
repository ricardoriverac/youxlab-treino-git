# Este arquivo serve para eu testar meus códigos e observar como eles se comportam,
# sem precisar escrever um código gigante.

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1

# valores = [5, 2, 5, 1, 1, 6]
# dobra(valores)
# print(f"Valores dobrados:", valores)

# def soma1(* valores):
#     s = 0
#     for numero in valores:
#         s += numero
#     print(f"\nSomando os valores {valores} temos {s}.\n")

# soma1(5, 2)
# soma1(2, 4)

# def lin():
#     print("-=-" * 10)

# def soma(texto, a, b):
#     lin()
#     print(texto.center(25))
#     lin()
#     print(f"\nValor A = {a}")
#     print(f"Valro B = {b}")
#     s = a + b
#     print(f"A soma de A + B = {s}\n")

# soma("Continha1", 1, 5)
# soma("Continha2", 2, 3)

# def contador(* numero):
#     for valor in numero:
#         print("Valor do contador:", valor)

# contador(4, 5, 6)
# contador(2, 1, 1)

# def ql():
#     print("\n")


# def cabecalho(texto):
#     largura = len(texto) + 15
#     print("~" * largura)
#     print(f"{texto.center(largura)}")
#     print("~" * largura)

# cabecalho("Teste de Titulo")

# ql()
# cabecalho("JOAO TESTES")
# ql()

# lst = [2,4,1]
# print(lst[1]) # Acessando o valor 1 da lista, referente ao número 4

# Tratamento de Erros e Exceções

# from random import randint
# from time import sleep

# try: # Tentar
#     sorteador = randint(1, 2)
#     print("\nSorteando de 1 a 2:")
#     sleep(2)
#     print("1 = Código correto.",
#           "2 = Código errado.")
#     sleep(3)
#     print(f"\nO valor sorteado foi {sorteador}.")

#     if sorteador == 1:
#         for q in range(6):
#             a = 0
#             a += 1
#             print(f"O Valor A, resulta em: {q}.")
#     else:
#         v += 1
# except Exception as erro: # Exceto, caso der problema | Excepetion(exeções) as(como) erro(variavel)
#     print(f"Problema encontrado foi {erro.__class__}") #erro(variavel).__class__ mostra a class de erro da excessão
# else: # Outro, Se o try deu certo
#     print("Deu certo")
# finally: #Finalização ou fechamento
#     print("Volte sempre! Muito obrigado!")

from random import randint

numPar = [2,4,6,8,10]
numIpar = [1,3,5,7,9]

computador = randint(numPar, numIpar)



print(f"O computador escolheu: {computador}")
