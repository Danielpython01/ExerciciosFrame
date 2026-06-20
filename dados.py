import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# --- Inserindo um único registro de forma segura ---
nome = "Ana Silva"
cargo = "Gerente de Projetos"
salario = 7500.00
# O comando SQL usa '?' como placeholders
comando_insert = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)"
# Os valores são passados em uma tupla no segundo argumento do execute()
cursor.execute(comando_insert, (nome, cargo, salario))


# --- Inserindo múltiplos registros de uma vez com executemany() ---
novos_funcionarios = [
    ('Carlos Souza', 'Desenvolvedor Pleno', 5200.00),
    ('Beatriz Costa', 'Analista de RH', 4800.00),
    ('Daniel Martins', 'Desenvolvedor Sênior', 8900.00)
]
cursor.executemany("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", novos_funcionarios)


# Salva (confirma) as mudanças no banco de dados
conexao.commit()
print("Dados inseridos com sucesso.")

conexao.close()