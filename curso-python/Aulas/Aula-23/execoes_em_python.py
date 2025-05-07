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