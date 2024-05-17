import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database = 'bdyoutube',
)

cursor = conexao.cursor()
#CRUD
#create 
nome_produto = "todynho"
valor = 3
comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando) 
conexao.commit() #edita o banco de dados
#resultado = cursor.fetchall() #ler banco de dados














cursor.close()
conexao.close()