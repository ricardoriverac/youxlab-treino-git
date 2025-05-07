# === MÓDULOS E PACOTES EM PYTHON ===

# MÓDULO:
# Um módulo é um arquivo .py com funções, variáveis ou classes que podemos importar em outros códigos.
# Exemplo: uteisJPSS.py é um módulo que criamos com funções úteis.

# Importando um módulo:
# import uteisJPSS

# PACOTE:
# Um pacote é uma pasta que contém vários módulos (.py).
# Para ser reconhecida como pacote, a pasta precisa de um arquivo __init__.py (pode estar vazio).

# Exemplo de estrutura de pacote:
# meu_pacote/
# ├── __init__.py
# ├── uteisJPSS.py
# └── matematica.py

# IMPORTAÇÃO:
# Podemos importar o módulo inteiro ou apenas partes dele:

# 1. Importar tudo do módulo:
# import uteisJPSS
# uteisJPSS.fatorial(5)

# 2. Importar só uma função:
# from uteisJPSS import fatorial
# fatorial(5)

# 3. Importar e dar um apelido (alias):
# import uteisJPSS as u
# u.fatorial(5)

# VANTAGENS DOS MÓDULOS E PACOTES:
# - Organização do código
# - Facilidade na manutenção
# - Ocultação de detalhes (usa sem saber como foi feito)
# - Reutilização em outros projetos
# - Melhor leitura e estruturação

# DICA:
# Crie seus próprios módulos sempre que tiver várias funções reutilizáveis!
# Nomeie os arquivos com nomes simples e sem espaços (ex: uteisJPSS.py)

# ================================

import uteisJPSS

titulo = uteisJPSS.cabecalho("Números")

entrada = input("Digite um número: ")

if entrada.isnumeric():
    num = int(entrada)
    print("Número válido.")

    par = uteisJPSS.parOuImpar(num)
    uteisJPSS.ql()

    fat = uteisJPSS.fatorial(num)
    print(f"O fatorial de {num} é {fat}.")
    print(f"O dobro de {num} é {uteisJPSS.dobro(num)}.")
    print(f"O triplo de {num} é {uteisJPSS.triplo(num)}.")

else:
    print("Você não digitou um número.")
