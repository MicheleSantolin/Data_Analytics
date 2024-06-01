import sqlite3

conexao = sqlite3.connect('exercicios_bd')
cursor = conexao.cursor()

# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
#cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

# Insira alguns registros de clientes na tabela.
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo)VALUES (1, "Roberta", 38, 45.5)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo)VALUES (2, "Letícia", 23, 250.5)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo)VALUES (3, "Glauber", 30, 79.5)')


conexao.commit()
conexao.close