import sqlite3

conexao = sqlite3.connect('exercicios_bd')
cursor = conexao.cursor()

#2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

# cursor.execute('INSERT INTO alunos(id, nome, idade, curso)VALUES (1, "Michele", 31, "Data Analytics")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso)VALUES (2, "Luana", 31, "Engenharia de Dados")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso)VALUES (3, "Paulo", 28, "Marketing Digital")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso)VALUES (4, "Euzébio", 42, "Sistemas de Informação")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso)VALUES (5, "Carol", 35, "Engenharia de Software")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso)VALUES (6, "Teste", 99, "Data Analytics")')


conexao.commit()
conexao.close