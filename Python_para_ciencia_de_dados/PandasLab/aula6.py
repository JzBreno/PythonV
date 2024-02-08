import numpy as np
import pandas as pd

from pandas import Series, DataFrame
# concatenando dados

df = pd.DataFrame(np.arange(36).reshape(6, 6))
df2 = pd.DataFrame(np.arange(15).reshape(5, 3))
print(df)
print('')
print(df2)
print('')

# df3 = pd.concat([df, df2]) considera o indice das colunas
df3 = pd.concat([df, df2], axis=1)  # considera o indice das linhas
print(df3)
