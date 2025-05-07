# Tratamento de Erros e Exceções em Python
# Aula do Curso em Vídeo - Gustavo Guanabara
# Documentação Oficial: https://docs.python.org/pt-br/3/tutorial/errors.html
# Aula: https://youtu.be/xz2B3bfNjEk?feature=shared

"""
Erros são inevitáveis em programas, mas podemos tratá-los para evitar que o programa quebre.
O tratamento de erros em Python é feito com try / except / else / finally.
"""

# ESTRUTURA BÁSICA
try:
    # Código que pode causar erro
    numero = int(input("Digite um número: "))
except:
    # Executa se der erro
    print("Você digitou um valor inválido.")
else:
    # Executa se não der erro
    print(f"Você digitou o número {numero}.")
finally:
    # Sempre executa
    print("Fim do programa.")

# É possível tratar erros específicos:
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Por favor, digite apenas números inteiros.")
except Exception as erro:
    print(f"Ocorreu um erro: {erro.__class__}")
else:
    print(f"O resultado é {r}")
finally:
    print("Encerrando...")

# EXEMPLO PRÁTICO MAIS COMPLETO
try:
    n = int(input("Digite um número inteiro: "))
    print(f"O dobro de {n} é {n * 2}")
except (ValueError, TypeError):
    print("Erro: você não digitou um número válido.")
except KeyboardInterrupt:
    print("\nO usuário preferiu não digitar os dados.")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
else:
    print("Executado com sucesso!")
finally:
    print("Operação finalizada.")

# --------------------------------------------

from random import randint
from time import sleep

try: # Tentar
    sorteador = randint(1, 2)
    print("\nSorteando de 1 a 2:")
    sleep(2)
    print("1 = Código correto.",
          "2 = Código errado.")
    sleep(3)
    print(f"\nO valor sorteado foi {sorteador}.")

    if sorteador == 1:
        for q in range(6):
            a = 0
            a += 1
            print(f"O Valor A, resulta em: {q}.")
    else:
        v += 1
except Exception as erro: # Exceto, caso der problema | Excepetion(exeções) as(como) erro(variavel)
    print(f"Problema encontrado foi {erro.__class__}") #erro(variavel).__class__ mostra a class de erro da excessão
else: # Outro, Se o try deu certo
    print("Deu certo")
finally: #Finalização ou fechamento
    print("Volte sempre! Muito obrigado!")

