# ======= RESUMÃO AULA 21 – FUNÇÕES PARTE 2 =======

# 1. AJUDA INTERATIVA (help)
# O Python tem um sistema de ajuda embutido. Use a função help() para saber como outras funções funcionam.

help(print)  # Mostra a documentação da função print
help(len)    # Mostra a documentação da função len

# 2. DOCSTRINGS (Documentação dentro da função)
# Podemos escrever uma descrição dentro da função para explicar o que ela faz.
# Basta usar aspas triplas logo após a definição.

def soma(a, b):
    """
    Soma dois valores e retorna o resultado.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Soma de a + b
    """
    return a + b

# Para ver a docstring:
help(soma)

# 3. PARÂMETROS OPCIONAIS (com valor padrão)
# Podemos definir valores padrão nos parâmetros.
# Se não passarmos valor, ele assume o padrão.

def apresentar(nome="Desconhecido", idade=0):
    print(f"Nome: {nome} | Idade: {idade}")

apresentar("João", 25)
apresentar("Maria")
apresentar()

# 4. ESCOPO DE VARIÁVEIS
# Variável GLOBAL: definida fora da função, pode ser usada em qualquer lugar do código.
# Variável LOCAL: definida dentro da função, só existe dentro dela.

def teste():
    x = 5  # variável local
    print("Dentro da função, x =", x)

x = 10  # variável global
teste()
print("Fora da função, x =", x)

# OBS: Se quiser modificar uma variável global dentro da função, use a palavra-chave 'global'

def alterar():
    global x
    x = 20
    print("Variável global x alterada dentro da função:", x)

alterar()
print("Novo valor de x fora da função:", x)

# 5. RETORNO DE VALORES (return)
# Uma função pode retornar um valor que pode ser usado fora dela.

def fatorial(n=1):
    """
    Calcula o fatorial de um número.
    :param n: Número para calcular o fatorial
    :return: Resultado do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

resultado = fatorial(5)
print("Fatorial de 5 é:", resultado)

# Também podemos retornar múltiplos valores em forma de tupla

def estatisticas(valores):
    """
    Recebe uma lista e retorna soma, média e quantidade de elementos.
    """
    total = sum(valores)
    media = total / len(valores)
    qtd = len(valores)
    return total, media, qtd

dados = [5, 8, 10]
s, m, q = estatisticas(dados)
print(f"Soma: {s}, Média: {m}, Quantidade: {q}")

# =============================================
# DICAS DA AULA:
# - Sempre documente suas funções com docstrings.
# - Use valores padrão para tornar funções mais flexíveis.
# - Cuidado com escopo de variáveis (global vs local).
# - Retornar valores com 'return' deixa o código mais organizado e útil.
# - Use help() para aprender mais sobre funções do Python ou as que você criou.

# Próxima aula: Prática com funções e parâmetros

# =============================================
