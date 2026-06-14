# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %%
df = pd.read_csv('../data/avengers.csv', encoding='ISO-8859-1')
df.head()
# %%
df.dtypes
# %%
df.info()
# %%
df.fillna({'Return1': 'NO'}, inplace=True)
# %%
total_nulos = df.isnull().sum()
total_linhas = len(df)
porcentagem = (total_nulos / total_linhas) * 100
porcentagem
# %%
df = df.drop(['Probationary Introl','Death2', 'Return2', 'Death3',
              'Return3', 'Death4', 'Return4', 'Death5', 'Return5',
              'Notes'], axis=1)
# %%
df.head()
# %%
df['Death1'] = df['Death1'].replace({'YES': 1, 'NO': 0})
# %%
df['Return1'] = df['Return1'].replace({'YES': 1, 'NO': 0})
# %%
df.describe()
# %%
