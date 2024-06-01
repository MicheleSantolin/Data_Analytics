import sqlite3

conexao = sqlite3.connect('exercicios_bd')
cursor = conexao.cursor()

# Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.
#cursor.execute('UPDATE alunos SET idade=32 WHERE id=1')

# b) Remova um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos WHERE id=3')



conexao.commit()
conexao.close