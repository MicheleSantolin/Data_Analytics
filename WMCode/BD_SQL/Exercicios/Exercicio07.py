import sqlite3

conexao = sqlite3.connect('exercicios_bd')
cursor = conexao.cursor()

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.

#cursor.execute('UPDATE clientes SET saldo=1001 WHERE id=1')

# b) Remova um cliente pelo seu ID.
# cursor.execute('DELETE FROM clientes WHERE id=3')

conexao.commit()
conexao.close