import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# criar dados

dados = np.arange(8)
print(dados)

# reorganizar dados com reshape

print(dados.reshape((4, 2)))
"""
apresentara desta forma
[[0 1] 
 [2 3] 
 [4 5] 
 [6 7]]

"""

indice = ['indice 1', 'indice 2', 'indice 3', 'indice 4',
          'indice 5', 'indice 6', 'indice 7', 'indice 8']

# selecionar e buscar dados

serie = Series(dados, index=indice)

print(serie)

"""
apresenatar desta forma
indice 1    0
indice 2    1
indice 3    2
indice 4    3
indice 5    4
indice 6    5
indice 7    6
indice 8    7
dtype: int32


"""

print(serie['indice 8'])  # mostrara o numero 7

# criar datframe e selecionar dados

np.random.seed(25)

indice = ['indice 1', 'indice 2', 'indice 3', 'indice 4',
          'indice 5', 'indice 6']
coluna = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4',
          'coluna 5', 'coluna 6']
df = DataFrame(np.random.rand(36).reshape(6, 6),
               index=indice,  # usando minha lçista de indices
               columns=coluna)  # usando minha lista de colunas

print(df)

# selecionar dados do dataframe, recebe linhas e colunaas
print('novo dataframe locado com df.loc')
print(df.loc[['indice 2', 'indice 4'], ['coluna 5', 'coluna 2']])

# fatiando dados

print(serie['linha 1': 'linha 7'])
