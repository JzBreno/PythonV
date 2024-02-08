import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#tranformações de dados

df = DataFrame(np.arange(36).reshape((6, 6))) #arange != random.rand
print(df)

print(df.drop([0]))  #drop se reecbe uma lista com as linhas que quero remover, retorna um dataframe, usando inplace, axis troca linha por colunas

#acrescentar novos dados a coluna

Serie = pd.Series(np.arange(6))
Serie.name = 'Nova_Variavel'

#cncatenando df e serie em novo df

novo_df = pd.DataFrame.join(df, Serie)
print(novo_df)

#ordenar linhas da coluna
print('')

print(novo_df.sort_values(by=['Nova_Variavel'], ascending=False))