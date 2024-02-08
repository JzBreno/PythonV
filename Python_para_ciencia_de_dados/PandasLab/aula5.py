import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# retirar valores duplicados
Dados = {
    'coluna': [1, 1, 2, 2, 3, 3, 3],
    'coluna 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'coluna 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']
}

df = DataFrame(Dados)
print(df)

#df.duplicated() retorna boolean de quais valores sao duplicados
print('')
print(df.duplicated())

df.drop_duplicates(inplace=True) #sem inplace=True, os valores nao serao alterados no dataframe original

print(df)
