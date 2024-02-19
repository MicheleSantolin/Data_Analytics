import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')



#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('DROP TABLE produtos')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone)VALUES (1,"Michele","França","micha@email.com",12345)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone)VALUES (2,"Maria","Ceu","maria@email.com",123456)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone)VALUES (3,"Luana","Bahia","luana@email.com",123457)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone)VALUES (4,"Pão de Ló","Padaria","paozin@email.com",123458)')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email)VALUES (1,"Michele","França","micha@email.com")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email)VALUES (1,"João","Espanha","jao@email.com")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email)VALUES (8,"Claudia","Castelo","clau@email.com")')



#cursor.execute('DELETE FROM usuario where id=1')
#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="Pão de Ló"')
#cursor.execute('UPDATE gerentes SET id="2" WHERE nome="João"')


# ORDER BY E DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
#for usuario in dados:
#    print(usuario)

# LIMIT E DISTINT
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2')
#for usuario in dados:
#    print(usuario)

# GROUP BT E HAVING
#dados = cursor.execute('SELECT nome FROM usuario  GROUP BY nome HAVING id>3')
#for usuario in dados:
#    print(usuario)

# JOIN'S
# JOIN INNER JOIN
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')
#for usuario in dados:
#    print(usuario)

# JOIN - LEFT JOIN
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')
#for usuario in dados:
#   print(usuario)

# JOIN - RIGHT JOIN
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.id')
#for usuario in dados:
#   print(usuario)

#JOIN - FULL JOIN
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')
#for usuario in dados:
#   print(usuario)

# SUB-CONSULTAS / SUB-QUERYS OU CONSULTAS SQL
dados = cursor.execute('SELECT * FROM usuariO WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
   print(usuario)

conexao.commit()
conexao.close