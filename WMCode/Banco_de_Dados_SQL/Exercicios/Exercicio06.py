import sqlite3

conexao = sqlite3.connect('exercicios_bd')
cursor = conexao.cursor()

#6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
# for clientes in dados:
#       print(clientes)

# b) Calcule o saldo médio dos clientes.
# dados = cursor.execute('SELECT saldo FROM clientes')

# total_saldos = 0
# numero_clientes = 0

# for linhas in cursor:
#     total_saldos += linhas[0]
#     numero_clientes += 1

# saldo_medio = total_saldos / numero_clientes if numero_clientes > 0 else 0
# print(saldo_medio)


# c) Encontre o cliente com o saldo máximo.

# dados = cursor.execute('SELECT saldo FROM clientes')
# saldo_max = 0
# cliente_max_saldo = None

# for linha in cursor:
#     saldo = linha[0]
#     if saldo > saldo_max:
#         saldo_max = saldo
#         cliente_max_saldo = linha
# if cliente_max_saldo:
#     print(cliente_max_saldo)
# else:
#     print("Nenhum cliente encontrado.")


# d) Conte quantos clientes têm saldo acima de 1000.
# cursor.execute('SELECT saldo FROM clientes WHERE saldo > 1000')
# qnt_clientes_saldo_acima_1000 = 0

# for linha in cursor:
#     qnt_clientes_saldo_acima_1000 += 1

# print(qnt_clientes_saldo_acima_1000)

conexao.commit()
conexao.close