import pypyodbc

dados_conexao = (
    "Driver = {SQL Server};",
    "Server = DESKTOP-8R0IJ69;",
    "DataBase = exercicio;"
)

conexao = pypyodbc.connect(dados_conexao)
