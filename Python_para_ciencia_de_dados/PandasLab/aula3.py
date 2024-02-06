# tratando valores em branco
"""
Descobrindo que esta faltando

Preenchendo valores em branco

Contando valores em branco

filtrando valores em branco

"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# encontrando valores em branco

in_white = np.nan

# criandp serie com valores em branco
serie = Series(['linha 1', 'linha 2', in_white, 'linha 4',
               'linha 5', 'linha 6', in_white, 'linha 8'])

# print(serie)

# nome_do_objeto.isnull() retorna objetos em branco

print(serie.isnull())

# preenchendo valores em branco
# criando dataframe
np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape((6, 6)))
# print(df)

df.loc[3:5, 0] = in_white  # loc colocara os valores novos no dataframe

# print(df)

# preencher os valores nan com obj.fillna(valor)
df_preenchido = df.fillna(0)
print(df)
print(df_preenchido)


dicio = {0: 0.1, 5: 1.25}
df_preenchido = df.fillna(dicio)
print(df_preenchido)
