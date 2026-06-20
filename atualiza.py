import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

novo_salario = 9200.00
nome_funcionario = "Ana Silva"

# A cláusula UPDATE modifica registros, e a WHERE especifica QUAL registro modificar
comando_update = "UPDATE funcionarios SET salario = ? WHERE nome = ?"
cursor.execute(comando_update, (novo_salario, nome_funcionario))

conexao.commit()
print(f"O salário de {nome_funcionario} foi atualizado.")

conexao.close()