import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# Comando SQL para criar uma tabela chamada 'funcionarios'
# INTEGER PRIMARY KEY AUTOINCREMENT: um ID numérico único que aumenta sozinho
# TEXT: para campos de texto
# NOT NULL: o campo não pode ser deixado em branco
comando_sql = """
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
);
"""

# Executa o comando
cursor.execute(comando_sql)
print("Tabela 'funcionarios' criada com sucesso.")

conexao.close()