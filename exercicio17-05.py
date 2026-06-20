import sqlite3
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()
titulo_para_deletar = "Dom Quixote"
cursor.execute("DELETE FROM livros WHERE titulo = ?", (titulo_para_deletar,))
conexao.commit()
print(f"O livro '{titulo_para_deletar}' foi removido.")
conexao.close()