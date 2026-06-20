import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QComboBox, QPushButton,
    QGridLayout
)
from PyQt6.QtCore import Qt


class CalculadoraFuturista(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Futurista")
        self.setFixedSize(500, 250)

        self.setStyleSheet("""
            QWidget {
                background-color: #0d1117;
            }

            QLineEdit {
                background-color: #161b22;
                color: #00ffff;
                border: 2px solid #00ffff;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
            }

            QComboBox {
                background-color: #161b22;
                color: #ff00ff;
                border: 2px solid #ff00ff;
                border-radius: 10px;
                padding: 6px;
                font-size: 16px;
            }

            QPushButton {
                background-color: #00ffff;
                color: black;
                border: none;
                border-radius: 12px;
                font-size: 18px;
                font-weight: bold;
                padding: 12px;
            }

            QPushButton:hover {
                background-color: #00cccc;
            }

            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
            }

            #resultado {
                background-color: #161b22;
                color: #39ff14;
                border: 2px solid #39ff14;
                border-radius: 12px;
                padding: 12px;
                font-size: 20px;
            }
        """)

        layout = QGridLayout()
        layout.setSpacing(15)

        self.num1 = QLineEdit()
        self.num1.setPlaceholderText("Primeiro número")

        self.num2 = QLineEdit()
        self.num2.setPlaceholderText("Segundo número")

        self.op = QComboBox()
        self.op.addItems(["+", "-", "*", "/"])

        self.botao = QPushButton("⚡ CALCULAR")
        self.botao.clicked.connect(self.calcular)

        self.resultado = QLabel("Resultado:")
        self.resultado.setObjectName("resultado")
        self.resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.num1, 0, 0)
        layout.addWidget(self.op, 0, 1)
        layout.addWidget(self.num2, 0, 2)

        layout.addWidget(self.botao, 1, 0, 1, 3)
        layout.addWidget(self.resultado, 2, 0, 1, 3)

        self.setLayout(layout)

    def calcular(self):
        try:
            n1 = float(self.num1.text())
            n2 = float(self.num2.text())
            operador = self.op.currentText()

            if operador == "+":
                res = n1 + n2
            elif operador == "-":
                res = n1 - n2
            elif operador == "*":
                res = n1 * n2
            elif operador == "/":
                if n2 == 0:
                    self.resultado.setText("❌ Divisão por zero")
                    return
                res = n1 / n2

            self.resultado.setText(f"✅ Resultado: {res:.2f}")

        except ValueError:
            self.resultado.setText("⚠ Entrada inválida")


app = QApplication(sys.argv)

janela = CalculadoraFuturista()
janela.show()

sys.exit(app.exec())