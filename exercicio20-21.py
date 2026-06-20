import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

def mudar_cor(cor):
    janela.setStyleSheet(f"background-color: {cor};")

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Mudar Cor")
layout = QHBoxLayout()

botao_vermelho = QPushButton("Vermelho")
botao_verde = QPushButton("Verde")
botao_azul = QPushButton("Azul")

# Usamos lambda para passar um argumento para a função
botao_vermelho.clicked.connect(lambda: mudar_cor("red"))
botao_verde.clicked.connect(lambda: mudar_cor("green"))
botao_azul.clicked.connect(lambda: mudar_cor("blue"))

layout.addWidget(botao_vermelho)
layout.addWidget(botao_verde)
layout.addWidget(botao_azul)
janela.setLayout(layout)
janela.show()
sys.exit(app.exec())