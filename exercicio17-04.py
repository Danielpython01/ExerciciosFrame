import sqlite3
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()
autor_busca = "George Orwell"
cursor.execute("SELECT * FROM livros WHERE autor = ?", (autor_busca,))
livro = cursor.fetchone() # .fetchone() busca apenas o primeiro resultado
if livro:
    print(f"Livro encontrado: {livro}")
else:
    print("Nenhum livro encontrado para este autor.")
conexao.close()