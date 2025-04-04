# Lista 2.0 em Python – Trabalhando com Listas Compostas

# Uma lista pode conter outras listas dentro dela. Chamamos isso de lista composta.
# Muito útil quando queremos agrupar dados relacionados, como nome e idade de uma pessoa.

# ---
# 1. Criando uma lista com dados variados

dados = list()
dados.append("Pedro")  # Nome
dados.append(25)        # Idade

print(dados[0])  # Saída: Pedro
print(dados[1])  # Saída: 25

# ---
# 2. Inserindo a lista 'dados' dentro de outra lista

pessoas = list()
pessoas.append(dados[:])  # Adiciona uma cópia da lista 'dados'

print(pessoas)  # Saída: [['Pedro', 25]]

# Usamos dados[:] para fazer uma CÓPIA dos dados, e não apenas uma referência
# Se usarmos pessoas.append(dados) sem [:], ambas variáveis apontariam para a mesma lista (ligadas)

# Podemos continuar adicionando outras pessoas:
dados[0] = "Maria"
dados[1] = 22
pessoas.append(dados[:])

print(pessoas)  # Saída: [['Pedro', 25], ['Maria', 22]]

# Acesso individual:
print(pessoas[0][0])  # Pedro
print(pessoas[1][1])  # 22
print(pessoas[0]) # Pedro, 25
