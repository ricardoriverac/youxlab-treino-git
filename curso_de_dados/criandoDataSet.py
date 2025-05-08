import pandas as pd
personagens = pd.DataFrame ({
    'nome': ['luke', 'palpatine', 'darthvader'],
    'idade': ['16', '70', '56'],
    'peso': [70.7, 12.5, 56.4],
    'é jedi': [True, False, False],
})

print(f'\n {personagens}')
print(personagens.info())
print(list(personagens.columns))

personagens_renomeado = personagens.rename(columns={
    'nome': 'Nome Completo',
    'idade': 'Idade',
})
print(personagens_renomeado)

personagens.rename(columns=['NOME', 'IDADE', 'PESO', 'ED_JEDI'])
print(personagens) 