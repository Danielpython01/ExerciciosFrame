import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

contador = 0

def incrementar():
    global contador
    contador += 1
    label_contador.setText(str(contador))

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Contador")
layout = QVBoxLayout()

label_contador = QLabel(str(contador))
label_contador.setStyleSheet("font-size: 24px;")

botao = QPushButton("Incrementar")
botao.clicked.connect(incrementar)

layout.addWidget(label_contador)
layout.addWidget(botao)
janela.setLayout(layout)
janela.show()
sys.exit(app.exec())