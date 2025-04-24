import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
dados = pd.DataFrame({
    'tempo': range(10),
    'vendas1': np.random.random(10),
    'vendas2': np.random.random(10),
    'vendas3': np.random.random(10)
})

variaveis = ['vendas1', 'vendas2', 'vendas3']

for var in variaveis:
    plt.figure()
    plt.bar(dados['tempo'], dados[var], color='red')
    plt.title(f'Gráfico de Barras - {var}')
    plt.xlabel('Tempo')
    plt.ylabel(var)
    plt.tight_layout()
    plt.show()   