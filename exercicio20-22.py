import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout

def calcular():
    try:
        n1 = float(num1.text())
        n2 = float(num2.text())
        operador = op.currentText()
        res = 0
        if operador == '+': res = n1 + n2
        elif operador == '-': res = n1 - n2
        elif operador == '*': res = n1 * n2
        elif operador == '/':
            if n2 == 0:
                resultado.setText("Erro: Divisão por zero")
                return
            res = n1 / n2
        resultado.setText(f"Resultado: {res}")
    except ValueError:
        resultado.setText("Erro: Entrada inválida")

app = QApplication(sys.argv)
janela = QWidget()
janela.setWindowTitle("Calculadora")
layout = QGridLayout()

num1 = QLineEdit()
num2 = QLineEdit()
op = QComboBox()
op.addItems(['+', '-', '*', '/'])
resultado = QLabel("Resultado:")
botao = QPushButton("Calcular")
botao.clicked.connect(calcular)

layout.addWidget(num1, 0, 0)
layout.addWidget(op, 0, 1)
layout.addWidget(num2, 0, 2)
layout.addWidget(botao, 1, 0, 1, 3)
layout.addWidget(resultado, 2, 0, 1, 3)
janela.setLayout(layout)
janela.show()
sys.exit(app.exec())