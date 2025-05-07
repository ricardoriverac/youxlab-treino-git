import pandas as pd
data = pd.read_csv('./curso_dados/datasets/GasPricesinBrazil_2004-2019 (1).csv')
print(type(data))
data.shape
print(f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')
data.info()

personagens_df = pd.DataFrame({
     'nome': ['Goku', 'Vegeta', 'Freeza'],
    'idade': [41, 40, 123],
    'peso': [90.32, 85.67, 60.1],
    'eh jedi': [True, True, False]
})
print(personagens_df)
print(personagens_df.info())
print(personagens_df.columns)