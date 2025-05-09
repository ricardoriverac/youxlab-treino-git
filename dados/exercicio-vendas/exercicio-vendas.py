import pandas as pd
df = pd.read_csv('/home/youx/projeto-git/youxlab-treino-git/dados/exercicio-vendas/exercicio_vendas.csv')
df.dropna(inplace=True)
