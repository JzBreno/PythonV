"""
Tipos de dados 

Numerico 

    discreto - numeros inteiros usados para contagem - numero de quartos em hotel, etc...
    continuo - numeros (R) usados em medição - altura, peso, etc ...

Categorico (dados que podem ter apenas um conjunto de valores que representam categoria/grupos)

    nominal - grupos de categorias(cor de cabelo, idiomas, generos lietrarios/ valores se ordem)
    ordinal - grupo de categorias com ordem(tamanho de roupa(P,M,G), escala de satisfacao(ruim, medio, bom))

Identificador
possui apenas um unico individuo por categoria

Outros tipos de dados:

Texto : String
- sinopse de um filme
- descricao de atuvo na bolsa

Datas: Strings que representam datas

"""
import pandas as pd

# excel = pd.read_excel("Pandas\Base.xlsx")
# excel.head() #mostra a cabeca do dataframe
# exibe as 5 primeiras linhas do data frame
# print(excel.info())
# print(excel.shape)

alunos_df = pd.DataFrame({
    'nome': ['luke', 'yoda', 'papatine'],
    'Idade': [16, 1000, 70],
    'peso': [70, 15, 60],
    'eh jedi': [True, True, False]
})


print(alunos_df.head())

# renomear colunas

renomeia = alunos_df.rename(columns={
    'nome': 'Nome Completo',  # renomeia a copluna de nome nome para Nome completo
    'idade': 'Idade'
})


#renomaer todas as colunas com uma lista

alunos_df.columns = ['NOME', 'IDADE', 'PESO', 'JEDI SIM OU NAO']

print(alunos_df)
