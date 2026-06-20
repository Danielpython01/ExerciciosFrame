import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# --- Lendo TODOS os funcionários ---
print("--- Todos os Funcionários ---")
cursor.execute("SELECT * FROM funcionarios")
todos_funcionarios = cursor.fetchall() # .fetchall() busca todos os resultados
for funcionario in todos_funcionarios:
    print(funcionario) # Cada resultado é uma tupla: (id, nome, cargo, salario)

# --- Buscando apenas desenvolvedores com salário > 6000 ---
print("\n--- Desenvolvedores com Salário > 6000 ---")
# A cláusula WHERE filtra os resultados
cursor.execute("SELECT nome, salario FROM funcionarios WHERE cargo LIKE '%Desenvolvedor%' AND salario > ?", (6000,))
devs_bem_pagos = cursor.fetchall()
for dev in devs_bem_pagos:
    print(f"Nome: {dev[0]}, Salário: R${dev[1]:.2f}")

conexao.close()