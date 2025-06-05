import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*Paulo190548',
    database='bdyoutube',

)

cursor = conexao.cursor()

# crud
nome_produto = "todynho"
valor = 3

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}",{valor})'
cursor.execute(comando)
conexao.commit()  # editar o banco dedados

cursor.closer()
# create


# read


# update


# delete
