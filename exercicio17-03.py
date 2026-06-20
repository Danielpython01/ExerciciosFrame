import sqlite3
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()
cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()
print("--- Catálogo da Biblioteca ---")
for livro in livros:
    print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}")
conexao.close()