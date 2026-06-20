import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

id_para_deletar = 3 # ID da Beatriz Costa

# A cláusula DELETE remove registros
comando_delete = "DELETE FROM funcionarios WHERE id = ?"
cursor.execute(comando_delete, (id_para_deletar,))

conexao.commit()
print(f"Funcionário com ID {id_para_deletar} foi removido.")

conexao.close()