# Resumão sobre Dicionários em Python

# Dicionários são coleções de dados organizadas por CHAVES e VALORES.
# Ao contrário das listas (que usam índices), dicionários usam CHAVES para acessar os dados.

# ---
# 1. Criando Dicionários

pessoa = {
    'nome': 'João',
    'idade': 30,
    'sexo': 'M'
}

print(pessoa['nome'])   # Saída: João
print(pessoa['idade'])  # Saída: 30

# ---
# 2. Adicionando e Modificando Itens

pessoa['peso'] = 80.5           # Adiciona nova chave 'peso'
pessoa['idade'] = 31            # Modifica valor da chave 'idade'

# ---
# 3. Removendo Itens

del pessoa['sexo']              # Remove a chave 'sexo'

# ---
# 4. Funções e Métodos úteis

print(pessoa.keys())    # Retorna as chaves
print(pessoa.values())  # Retorna os valores
print(pessoa.items())   # Retorna os pares (chave, valor)

# ---
# 5. Percorrendo Dicionário

for chave in pessoa:
    print(f'{chave} = {pessoa[chave]}')

for chave, valor in pessoa.items():
    print(f'{chave} tem valor {valor}')

# ---
# 6. Lista de Dicionários (Estrutura composta)

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])  # Saída: Rio de Janeiro
print(brasil[1]['sigla'])  # Saída: SP

# ---
# 7. Cópia Correta de Dicionários

estado = dict()
brasil = list()

for i in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())  # Usar .copy() para evitar ligação entre os dicionários

# Exibindo dados:
for e in brasil:
    for chave, valor in e.items():
        print(f'O campo {chave} tem valor {valor}')
