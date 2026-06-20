import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def mostrar_saudacao():
    nome = campo_nome.text()
    label_saudacao.setText(f"Olá, {nome}!")

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Boas-Vindas")
layout = QVBoxLayout()

campo_nome = QLineEdit()
campo_nome.setPlaceholderText("Digite seu nome")

label_saudacao = QLabel("")

botao = QPushButton("Dizer Olá")
botao.clicked.connect(mostrar_saudacao)

layout.addWidget(campo_nome)
layout.addWidget(botao)
layout.addWidget(label_saudacao)
janela.setLayout(layout)
janela.show()
sys.exit(app.exec())