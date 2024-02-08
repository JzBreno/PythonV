import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# contar objetos em branco

in_white = np.nan
np.random.seed(25)

df = DataFrame(np.random.rand(36).reshape((6, 6)))

df.loc[3:5, 0] = in_white  # loc colocara os valores novos no dataframe
df.loc[1:4, 5] = in_white
# retorna uma serie com (coluna, qtd valores em branco)
print('DataFrame com valores em branco NaN')
print(df)
print('colunas e qtd de erros')
print(df.isnull().sum())
print('conjunto de linhas e colunas que nao apresentam valores em branco')
df1 = df.dropna(axis=1)
print(df1) #esses parametro passa a coluna e removera a coluna
