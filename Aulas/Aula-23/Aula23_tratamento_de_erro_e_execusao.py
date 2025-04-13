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

# --------------------------------------------
# PRINCIPAIS EXCEÇÕES EM PYTHON
# (Retirado da documentação oficial e exemplos práticos)

# ZeroDivisionError: Divisão por zero
# ValueError: Valor inválido (ex: ao converter string para int)
# TypeError: Operações com tipos incompatíveis
# IndexError: Índice fora do alcance em listas/tuplas
# KeyError: Chave inexistente em dicionário
# NameError: Variável não definida
# FileNotFoundError: Arquivo não encontrado
# ImportError: Módulo não encontrado ou erro ao importar
# AttributeError: Objeto não possui determinado atributo
# OverflowError: Número muito grande para ser representado
# MemoryError: Falta de memória
# IndentationError: Erro de indentação (tabulação)
# SyntaxError: Erro de sintaxe
# RuntimeError: Erro genérico em tempo de execução
# Exception: Classe base para todas as exceções padrão

# DICA: Você pode capturar todas as exceções com "except Exception as erro"
# e usar "erro.__class__" ou "type(erro)" para identificar qual foi o erro

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

# FIM DO RESUMO
