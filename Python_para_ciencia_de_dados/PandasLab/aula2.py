#criando e comparando valores com DataFrames e Series

import pandas as pd
import numpy as np

from pandas import Series, DataFrame

np.random.seed(25)  # padronizar randonização

indices = ['indice 1', 'indice 2', 'indice 3', 'indice 4',
           'indice 5', 'indice 6']  # lista de indices

colunas = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4',
           'coluna 5', 'coluna 6']  # listas de colunas


df = DataFrame(np.random.rand(36).reshape(
    6, 6), index=indices, columns=colunas)

# criando objeto para fazer cpmparção
indice = ['indice 1', 'indice 2', 'indice 3', 'indice 4',
          'indice 5', 'indice 6', 'indice 7', 'indice 8']

series_obj = Series(np.arange(8), index=indice)
filtro = series_obj > 6
print('A serie Completa')
print('')
print(series_obj)
print('')
print('Filtrado por Serie > 6')
print('')
print(series_obj[filtro])

# trcoando valores de listas com indices

series_obj['indice 1'] = 7
print(series_obj)
