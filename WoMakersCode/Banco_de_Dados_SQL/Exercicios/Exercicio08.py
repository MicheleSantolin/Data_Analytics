import sqlite3

conexao = sqlite3.connect('exercicios_bd')
cursor = conexao.cursor()

# 8. Junção de Tabelas

# a) Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). 

# cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto TEXT, valor REAL, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')


# b) Insira algumas compras associadas a clientes existentes na tabela "clientes".

# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES \
# (3, 1, "Barra de Chocolate", 11.45), \
# (2, 1, "Sabonete Facial", 25.50)')

# c) Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

# cursor.execute('''
#                 SELECT c.nome, co.produto, co.valor
#                 FROM clientes c
#                 JOIN compras co ON c.id = co.id
# ''')
# resultados = cursor.fetchall()

# for resultado in resultados:
#     print(resultado)

conexao.commit()
conexao.close