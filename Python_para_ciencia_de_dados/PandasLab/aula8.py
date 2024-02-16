import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#agrupar dados e estudalos 

carros = pd.read_csv('Python_para_ciencia_de_dados/PandasLab/carros.csv')
print(carros.head(5))

#rename
print('')
carros.columns = carros.columns = ['nomes','mpg','cyl','disp', 'hpt', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

print(carros.head(5))

#agrpando colunas
coluna_agrupamento = carros['cyl']
grupos_carros = carros.groupby(coluna_agrupamento)
print(grupos_carros.mean())

carros.columns = ['nomes', 'mpg', 'cyl','disp', 'hpt', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
grupos_carros = carros.groupby('cyl')
coluna = carros['cyl']
grupos_carros = carros.groupby(coluna)